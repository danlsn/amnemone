from functools import cached_property
from pathlib import Path

from amnemone.models import MnemonicList

BIP39_SUPPORTED_LANGUAGES = {
    'chinese_simplified',
    'chinese_traditional',
    'czech',
    'english',
    'french',
    'italian',
    'japanese',
    'korean',
    'portuguese',
    'russian',
    'spanish',
    'turkish',
}
SHORT_BIP39_SUPPORTED_LANGUAGES = {'english', 'spanish', 'french', 'italian', 'czech', 'portugese'}


class LanguageNotSupportedError(Exception):
    pass


class ShortBip39NotSupportedError(Exception):
    pass


class Bip39(MnemonicList):
    def __init__(self, language: str = 'english', **kwargs):
        if language not in BIP39_SUPPORTED_LANGUAGES:
            msg = f'BIP39 Language {language} not supported'
            raise LanguageNotSupportedError(msg)
        self.language = language
        super().__init__(self.words, reversed=kwargs.get('reversed', False))

    @cached_property
    def words(self):
        with open(Path(__file__).parent / f'{self.language}.txt', encoding='utf-8') as file:
            return file.read().splitlines()


class Bip39Short(MnemonicList):
    def __init__(self, language: str = 'english', **kwargs):
        if language not in SHORT_BIP39_SUPPORTED_LANGUAGES:
            msg = f'BIP39 Language {language} not supported'
            raise ShortBip39NotSupportedError(msg)
        self.language = language
        super().__init__(self.words, reversed=kwargs.get('reversed', False))

    @cached_property
    def words(self):
        with open(Path(__file__).parent / f'{self.language}.txt', encoding='utf-8') as file:
            return [w[:4] for w in file.read().splitlines()]
