import re
from typing import List

from vocabulary import Vocabulary


class GameEngine:

    def __init__(self):
        self.table = [['0' for _ in range(5)] for _ in range(5)]
        self.player_score = 0
        self.computer_score = 0
        self.sqr_for_computer: List[tuple] = [(i, x) for x in range(5) for i in [1, 3]]

    def input(self):
        valid = False
        while not valid:
            char, i, j = input("Введите букву, ряд и столбец: ").split()
            if len(char) == 1 and re.search(r'[а-яА-Я]', char):
                if self.table[int(i)][int(j)].isalpha():
                    print("Данная клетка занята.", end=' ')
                else:
                    valid = True
            else:
                print('Неверный ввод.', end=' ')
        self.table[int(i)][int(j)] = char.upper()
        return int(i), int(j)

    def start(self):
        word = Vocabulary.find_word(r'[а-яА-Я]{5}$', 5)
        self.table[2] = list(word.upper())

    @staticmethod
    def game_over_check(table):
        for raw in table:
            for square in raw:
                if not square.isalpha():
                    return False
        return True

    def draw_table(self):
        for raw in self.table:
            print(*raw, sep=' | ', end='\n')
        print('Ваш счёт: ', self.player_score)

    def highlight_word(self, player_i: int, player_j: int):
        while True:
            sqr_validation = False
            neigh_validation = True
            seq = input('Введите номера клеток через запятую для составления слова.').split(',')
            word = ''
            for t in range(len(seq)):
                i, j = seq[t].split()
                i_tmp, j_tmp = seq[t - 1].split()
                if (int(i), int(j)) == (player_i, player_j):
                    sqr_validation = True
                if t != 0 and abs(int(i) - int(i_tmp)) + abs(int(j) - int(j_tmp)) != 1:
                    neigh_validation = False
                word += self.table[int(i)][int(j)]
            if sqr_validation and neigh_validation:
                return word
            else:
                print("Ошибка.")

    def check_word(self, player_word, player_i, player_j):
        if Vocabulary.find_word(player_word, len(player_word)):
            Vocabulary.add_black_list(player_word)
            return True
        else:
            self.table[player_i][player_j] = '0'
            return False


class PlayGame(GameEngine):

    def play(self):
        self.start()
        while True:
            while True:
                self.draw_table()
                player_i, player_j = self.input()
                player_word = self.highlight_word(player_i, player_j)
                if not self.check_word(player_word, player_i, player_j):
                    print("Такого слова не существует или оно уже использовано.")
                else:
                    self.player_score += len(player_word)
                    break
            if self.game_over_check(self.table):
                break
