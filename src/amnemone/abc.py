from abc import ABC
from dataclasses import dataclass
from functools import cached_property
from typing import List, TypeVar, Iterable

from bidict import bidict, OrderedBidict

T = TypeVar('T', bound='WordList')


@dataclass
class WordList:
    def __init__(self, words: List[str] = None):
        self._words: List[str] = words or []
        self._index: OrderedBidict[int, str] = OrderedBidict({i: word for i, word in enumerate(self._words)})
        self._radix: int = len(self._words)

    def __getitem__(self, item):
        return self._words[item]

    def _set_words(self, words: Iterable[str]) -> List[str]:
        self._words = words
        self._index = OrderedBidict({i: word for i, word in enumerate(self._words)})
        self.radix = len(self.words)
        return self.words

    def _new_words(self, words: List[str]) -> List[str]:
        return [_ for _ in words if _ not in self._index.values()]

    @property
    def words(self) -> List[str]:
        return self._words

    @words.setter
    def words(self, words: List[str]) -> None:
        self._set_words(words)

    def extend(self, words: List[str]) -> None:
        if set(words).intersection(self.words):
            raise ValueError('Words must be unique')
        self._set_words(self.words + words)

    def add_words(self, *words: str) -> T:
        self.extend(list(words))
        return self

    @property
    def radix(self) -> int:
        return self._radix

    @radix.setter
    def radix(self, value: int) -> None:
        self._radix = value

    @cached_property
    def radix(self) -> int:
        return self._radix

    @cached_property
    def is_unique(self) -> bool:
        return len(self.words) == len(set(self.words))

    def sort(self, key: callable = str.casefold, reverse: bool = False) -> None:
        self.words = sorted(self.words, key=key, reverse=reverse)

    def encode(self, input_: List[int]) -> List[str]:
        return [self.words[i] for i in input_]

    def decode(self, input_: List[str]) -> List[int]:
        return [self._index.inverse[word] for word in input_]
