words = set()

with open('russian_nouns.txt', 'r', encoding='utf-8') as f:
    word = f.readline()
    while word:
        words.add(word[:-1])
        word = f.readline()
