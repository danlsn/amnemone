import json
from pathlib import Path


def an_array_of_english_words():
    with open(Path(__file__).parent / 'an-array-of-english-words.json', 'r') as file:
        return json.load(file)