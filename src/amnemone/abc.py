from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterable, TypeVar, Optional

from bidict import OrderedBidict

T = TypeVar('T', bound='WordList')


@dataclass
class WordList:
    _words: list[str]
    _index: OrderedBidict[int, str] = field(init=False, default_factory=OrderedBidict)
    _radix: int = 0

    def __init__(self, words: Optional[Iterable[str]] = None):
        self._set_words(words or [])

    def __getitem__(self, item):
        return self._words[item]

    def _set_words(self, words: Iterable[str]) -> list[str]:
        self._words = list(words)
        self._index = OrderedBidict({i: word for i, word in enumerate(self._words)})
        self.radix = len(self.words)
        return self.words

    def _new_words(self, words: list[str]) -> list[str]:
        return [_ for _ in words if _ not in self._index.values()]

    @property
    def words(self) -> list[str]:
        return self._words

    @words.setter
    def words(self, words: list[str]) -> None:
        self._set_words(words)

    def extend(self, words: list[str]) -> None:
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

    def encode(self, input_: list[int]) -> list[str]:
        return [self.words[i] for i in input_]

    def decode(self, input_: list[str]) -> list[int]:
        return [self._index.inverse[word] for word in input_]
