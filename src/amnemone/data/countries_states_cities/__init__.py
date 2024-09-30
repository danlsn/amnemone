from __future__ import annotations

import csv

__ALL__ = ['Cities', 'Countries', 'regions', 'states', 'subregions']

from functools import cached_property
from pathlib import Path

from amnemone.models import MnemonicList

CITIES_CSV_KEYS = ['id', 'name']
COUNTRIES_CSV_KEYS = ['id', 'name', 'iso3', 'iso2', 'numeric_code', 'native', 'emoji']


class KeyNotValidError(Exception):
    pass


def countries():
    with open(Path(__file__).parent / 'countries.csv', encoding='utf-8') as f:
        yield from csv.DictReader(f)


def regions():
    with open(Path(__file__).parent / 'regions.csv', encoding='utf-8') as f:
        yield from csv.DictReader(f)


def states():
    with open(Path(__file__).parent / 'states.csv', encoding='utf-8') as f:
        yield from csv.DictReader(f)


def subregions():
    with open(Path(__file__).parent / 'subregions.csv', encoding='utf-8') as f:
        yield from csv.DictReader(f)


class Cities(MnemonicList):
    def __init__(self, key: str = 'name', **kwargs):
        if key not in CITIES_CSV_KEYS:
            msg = f'key must be one of {CITIES_CSV_KEYS}'
            raise KeyNotValidError(msg)
        self._key: str = key
        super().__init__(self.words, reversed=kwargs.get('reversed', False))

    @cached_property
    def words(self) -> list[str]:
        with open(Path(__file__).parent / 'cities.csv', encoding='utf-8') as f:
            # noinspection PyTypeChecker
            return [row[self._key] for row in csv.DictReader(f)]


class Countries(MnemonicList):
    def __init__(self, key: str = 'name', **kwargs):
        if key not in COUNTRIES_CSV_KEYS:
            msg = f'key must be one of {COUNTRIES_CSV_KEYS}'
            raise KeyNotValidError(msg)
        self._key: str = key
        super().__init__(self.words, reversed=kwargs.get('reversed', False))

    @cached_property
    def words(self) -> list[str]:
        with open(Path(__file__).parent / 'countries.csv', encoding='utf-8') as f:
            # noinspection PyTypeChecker
            return [row[self._key] for row in csv.DictReader(f)]
