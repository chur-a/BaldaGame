import random

from game import GameEngine


class AI(GameEngine):

    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.alphabet = ['a', 'б', 'в', "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с",
                         "т", "У", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

    def add_sqr_for_computer(self, player_i: int, player_j: int):
        self.sqr_for_computer.remove((player_i, player_j))
        for i, j in self.moves:
            i_tmp, j_tmp = player_i + i, player_j + j
            if 0 <= i_tmp <= 4 and 0 <= j_tmp <= 4 and self.table[i_tmp][j_tmp] == '0':
                self.sqr_for_computer.append((i_tmp, j_tmp))

    def add_word(self):
        pass
