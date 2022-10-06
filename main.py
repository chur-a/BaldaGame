import game
from vocabulary import Vocabulary

instance = game.Game()
instance.play()

inst = Vocabulary()
print(inst.find_word(r'(ко[А-Яа-я]ка)$', 5))


