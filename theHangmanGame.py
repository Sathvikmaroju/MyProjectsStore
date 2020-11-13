import random

def hangman():
    wordsList = ['hangman', 'python']
    word, turns, guessmade, validEntries = random.choice(wordsList), 10, '', set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        main_word, missed = '', 0
        for letter in word:
            if letter in guessmade: main_word += letter
            else: main_word += '_ '
        if main_word == word:
            print(main_word, "\nYou won")
            break
        guess=input(f'guess the word {main_word}\n')
        if guess in validEntries: guessmade += guess
        else: guess = input('Invalid!\nguess the word ')
        if guess not in word:
            turns, line = turns-1, "-"*10
            pic = [f"9 turns left!\n{line}", f"8 turns left!\n{line}\n     o    ",
            f"7 turns left!\n{line}\n     o    \n     |    ", f"6 turns left!\n{line}\n     o    \n     |    \n    /     ",
            f"5 turns left!\n{line}\n     o    \n     |    \n    / \   ", f"4 turns left!\n{line}\n     o    \n    /|    \n    / \   ",
            f"3 turns left!\n{line}\n     o    \n    /|\   \n    / \   ", f"2 turns left!!\n{line}\n    \o/   \n     |    \n    / \   ",
            f"1 turn left!!!\nHangmaan on his last breath\n{line}\n     |    \n    \o/   \n     |    \n    / \   ",
            f"0 You loose\nYou let a good man die.\n{line}\n     o_|  \n    /|\   \n    / \   "]
            for i in pic:
                if turns == int(i[:1]): print(i)
            if turns == int(pic[-1][:1]) == 0 :
                    print(pic[-1][2:])
                    break

print("-"*45, "\nThe hang man game \nTry to guess the word in less than 10 attempts.")
hangman()