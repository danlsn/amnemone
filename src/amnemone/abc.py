from abc import ABC
from functools import cached_property
from typing import List, TypeVar

from bidict import bidict

T = TypeVar('T', bound='WordList')


class WordList(ABC):
    def __init__(self, words: List[str]):
        self._raw: List[str] = words
        self.words: bidict = bidict({i: word for i, word in enumerate(words)})

    @cached_property
    def radix(self) -> int:
        return len(self.words)

    @cached_property
    def is_unique(self) -> bool:
        return len(self.words) == len(set(self.words))

    def sort(self, key: callable = str.casefold) -> None:
        self.words = bidict({i: word for i, word in enumerate(sorted(self._raw, key=key))})

    def encode(self, input_: List[int]) -> List[str]:
        return [self.words[i] for i in input_]

    def decode(self, input_array: List[str]) -> List[int]:
        return [self.words.inverse[word] for word in input_array]
