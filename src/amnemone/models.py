from __future__ import annotations

import base64
import random
from dataclasses import dataclass
from functools import cached_property


@dataclass
class MnemonicList:
    words: list[str]
    reversed: bool = False

    def __post_init__(self):
        if self.reversed:
            self.words = self.words[::-1]

    @cached_property
    def radix(self):
        return len(self.words)

    def random(self, n: int = 1) -> list[str]:
        return random.choices(self.words, k=n)  # noqa: S311

    def from_int(self, n: int) -> list[str]:
        output = []
        if n < self.radix:
            return [self.words[n]]
        while n:
            n, r = divmod(n, self.radix)
            output.append(self.words[r])
        return output

    def from_hex(self, hex_string: str) -> list[str]:
        return self.from_int(int(hex_string, 16))

    def from_base64(self, base64_string: str) -> list[str]:
        return self.from_int(int.from_bytes(base64.b64decode(base64_string), 'big'))

    def _encode(self, input_: list[int]):
        return [self.words[i] for i in input_]

    def _decode(self, input_array: list[str | bytes]):
        return [self.words.index(word) for word in input_array]
