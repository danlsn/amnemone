import json


def an_array_of_english_words():
    with open('./an-array-of-english-words.json', 'r') as file:
        return json.load(file)