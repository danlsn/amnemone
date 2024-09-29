import csv

__ALL__ = ['cities', 'countries', 'regions', 'states', 'subregions']

from pathlib import Path


def cities():
    with open(Path(__file__).parent / 'cities.csv', encoding='utf-8') as f:
        yield from csv.DictReader(f)


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
