import hashlib
from pathlib import Path

from amnemone.data.bip39 import Bip39


def main():
    mn = Bip39()
    mn_short = Bip39(short=True)
    mn_rev = Bip39(reversed=True)

    with open(Path(__file__).parent / 'english.txt', encoding='utf-8') as file:
        md5_hash = hashlib.md5(file.read().encode()).hexdigest()  # noqa: S324

    print(md5_hash)
    for _ in [mn, mn_short, mn_rev]:
        print(_.from_hex(md5_hash))

    print(mn.from_int(1234567890))
    print(mn_short.from_int(1234567890))
    print(mn_rev.from_int(1234567890))

    print(mn.radix)
    print(mn.random(5))
    print(mn.from_int(1234567890))
    print(mn.from_hex('499602d2'))


if __name__ == '__main__':
    main()
