import csv
from collections import namedtuple
from functools import cached_property
from pathlib import Path

from amnemone.models import MnemonicList


class Afinn111(MnemonicList):
    def __init__(self):
        super().__init__(self.words)

    @cached_property
    def words(self) -> list[str]:
        with open(Path(__file__).parent / 'AFINN-111.txt', encoding='utf-8') as f:
            words = set()
            for row in csv.reader(f, delimiter='\t'):
                words.add(row[0])
            return sorted(words)

