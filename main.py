from ai import AI


engine = AI()


def play():
    engine.start()
    while True:
        while True:
            engine.draw_table()
            player_i, player_j = engine.input()
            player_word = engine.highlight_word(player_i, player_j)
            if not engine.check_word(player_word):
                engine.table[player_i][player_j] = '0'
                print("Такого слова не существует или оно уже использовано.")
            else:
                engine.player_score += len(player_word)
                engine.add_sqr_for_computer(player_i, player_j)
                break
        engine.draw_table()
        ai_letter, ai_i, ai_j, word = engine.add_word()
        engine.table[ai_i][ai_j] = ai_letter
        engine.computer_score += len(word)
        engine.add_sqr_for_computer(ai_i, ai_j)
        if engine.game_over_check(engine.table):
            break


play()
