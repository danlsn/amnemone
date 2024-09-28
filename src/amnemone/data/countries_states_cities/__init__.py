import csv

__ALL__ = ['cities', 'countries', 'regions', 'states', 'subregions']

from pathlib import Path


def cities():
    with open(Path(__file__).parent / 'cities.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def countries():
    with open(Path(__file__).parent / 'countries.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def regions():
    with open(Path(__file__).parent / 'regions.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def states():
    with open(Path(__file__).parent / 'states.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def subregions():
    with open(Path(__file__).parent / 'subregions.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row
