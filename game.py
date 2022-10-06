import re

from vocabulary import Vocabulary


class Game:

    def __init__(self):
        self.table = [['0' for _ in range(5)] for _ in range(5)]

    def draw(self):
        for raw in self.table:
            print(*raw, sep=' | ', end='\n')

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

    @staticmethod
    def game_over_check(table):
        for raw in table:
            for square in raw:
                if not square.isalpha():
                    return False
        return True

    def start(self):
        word = Vocabulary.find_word(r'[а-яА-Я]{5}$', 5)
        self.table[2] = list(word.upper())

    def play(self):
        self.start()
        while True:
            self.draw()
            self.input()
            if self.game_over_check(self.table):
                break

