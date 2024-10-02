import string
from typing import List

import pytest

from amnemone.abc import WordList


@pytest.fixture
def ascii_upper_wordlist() -> WordList:
    return WordList([*string.ascii_uppercase])


def test_wordlist_radix(ascii_upper_wordlist):
    wl = ascii_upper_wordlist
    assert wl.radix == 26


def test_wordlist_get_first_word(ascii_upper_wordlist):
    wl = ascii_upper_wordlist
    assert wl[0] == 'A'


def test_wordlist_get_last_word(ascii_upper_wordlist):
    wl = ascii_upper_wordlist
    assert wl[-1] == 'Z'


def test_wordlist_get_word_out_of_bounds(ascii_upper_wordlist):
    wl = ascii_upper_wordlist
    with pytest.raises(IndexError):
        var = wl[26]


def test_wordlist_set_words(ascii_upper_wordlist):
    wl = ascii_upper_wordlist
    wl.words = ['A', 'B', 'C']
    assert wl.words == ['A', 'B', 'C']
    assert wl.radix == 3


def test_wordlist_add_words_args(ascii_upper_wordlist):
    wl = ascii_upper_wordlist
    wl.words = ['A', 'B', 'C']
    assert wl.words == ['A', 'B', 'C']
    assert wl.radix == 3
    wl.add_words('D', 'E')
    assert wl.words == ['A', 'B', 'C', 'D', 'E']
    assert wl.radix == 5


def test_wordlist_add_words_list(ascii_upper_wordlist):
    wl = ascii_upper_wordlist
    wl.words = ['A', 'B', 'C']
    assert wl.words == ['A', 'B', 'C']
    assert wl.radix == 3
    with pytest.raises(TypeError):
        wl.add_words(['D', 'E']) # noqa
    wl.extend(['D', 'E'])
    assert wl.words == ['A', 'B', 'C', 'D', 'E']
    assert wl.radix == 5


def test_sort_shuffled_wordlist(ascii_upper_wordlist):
    wl = ascii_upper_wordlist
    shuffled_wl = wl.words.copy()
    import random
    random.shuffle(shuffled_wl)
    wl.words = shuffled_wl
    wl.sort()
    assert wl.words == [*string.ascii_uppercase]


def test_sort_wordlist_reverse_alphabet(ascii_upper_wordlist):
    wl = ascii_upper_wordlist
    wl.sort(reverse=True)
    assert wl.words == [*string.ascii_uppercase][::-1]
    assert wl.radix == 26



