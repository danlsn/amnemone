from amnemone.data.bip39 import Bip39, Bip39Short


def test_bip39_radix():
    mn = Bip39()
    assert mn.radix == 2048
    mn_short = Bip39Short()
    assert mn_short.radix == 2048
    mn_rev = Bip39(reversed=True)
    assert mn_rev.radix == 2048


def test_bip39_random():
    mn = Bip39()
    assert len(mn.random(5)) == 5
    mn_short = Bip39Short()
    assert len(mn_short.random(5)) == 5
    mn_rev = Bip39(reversed=True)
    assert len(mn_rev.random(5)) == 5


def test_bip39_from_hex():
    hex_input = 'f23506956964fa69c98fa3fb5c8823b5'
    expected_words = [
        'issue',
        'calm',
        'purity',
        'distance',
        'butter',
        'include',
        'spy',
        'gossip',
        'pudding',
        'bottom',
        'box',
        'august',
    ]
    mn = Bip39()
    assert mn.from_hex(hex_input) == expected_words
    mn_short = Bip39Short()
    assert mn_short.from_hex(hex_input) == [w[:4] for w in expected_words]
