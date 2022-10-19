import random
from typing import List, Tuple

from game import GameEngine
from vocabulary import Vocabulary


class AI(GameEngine):

    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.alphabet = ['a', 'б', 'в', "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с",
                         "т", "У", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
        self.word_length = [4, 5, 6, 7]
        self.weights = [40, 30, 10, 5]

    def add_sqr_for_computer(self, player_i: int, player_j: int):
        self.sqr_for_computer.remove((player_i, player_j))
        for i, j in self.moves:
            i_tmp, j_tmp = player_i + i, player_j + j
            if 0 <= i_tmp <= 4 and 0 <= j_tmp <= 4 and \
                    self.table[i_tmp][j_tmp] == '0' and (i_tmp, j_tmp) not in self.sqr_for_computer:
                self.sqr_for_computer.append((i_tmp, j_tmp))

    def collect_word(self, word: str, word_length: int, start_i: int,
                     start_j: int, used_sqr: List[Tuple[int, int]] = []):
        if len(word) >= word_length:
            yield word
        else:
            for move in self.moves:
                i = start_i + move[0]
                j = start_j + move[1]
                if 0 <= i < 5 and 0 <= j < 5 and (i, j) not in used_sqr and self.table[i][j] != '0':
                    word += self.table[i][j]
                    used_sqr.append((i, j))
                    yield from self.collect_word(word, word_length, i, j, used_sqr)
                    word = word[:-1]
                    used_sqr.pop()

    def find_word(self, start_i: int, start_j: int, length: int):
        for letter in self.alphabet:
            for word in self.collect_word(letter, length, start_i, start_j):
                if Vocabulary.find_word(word.lower(), len(word)) and word.lower() not in Vocabulary.BlackList:
                    return letter, word
                elif Vocabulary.find_word(word[::-1].lower(), len(word)) and \
                        word[::-1].lower() not in Vocabulary.BlackList:
                    return letter, word[::-1]

    def compute(self):
        length = random.choices(self.word_length, weights=self.weights, k=1)[0]
        while True:
            for i, j in self.sqr_for_computer:
                result = self.find_word(i, j, length)
                if result:
                    return result[0], result[1], i, j
            length -= 1

    def add_word(self):
        letter, word, i, j = self.compute()
        Vocabulary.add_black_list(word)
        return letter.upper(), i, j, word
