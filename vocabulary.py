import re
from abc import ABC


class CreateVoc(ABC):

    @staticmethod
    def create(vocabulary: dict):
        with open('russian_nouns.txt', 'r', encoding='utf-8') as f:
            word = f.readline()
            while word:
                if len(word) - 1 in vocabulary:
                    vocabulary[len(word) - 1].add(word[:-1])
                else:
                    vocabulary[len(word) - 1] = set(word[:-1], )
                word = f.readline()
        return vocabulary


class Vocabulary(CreateVoc):

    Words = CreateVoc.create(dict())
    BlackList = set()

    @classmethod
    def find_word(cls, pattern: str, length: int):
        pattern = pattern.lower()
        for word in cls.Words[length]:
            result = re.match(pattern, word)
            if result and result.string not in cls.BlackList:
                return result.string

    @classmethod
    def add_black_list(cls, word: str):
        cls.BlackList.add(word.lower())

    def ret(self):
        return self.Words
