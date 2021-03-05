# -*- coding: utf-8 -*-

import random

def play():
    print("*********************************")
    print("***Welcome to SPELLING WORDS game!***")
    print("*********************************")


    arch = open("words.txt", "r")
    words = []

    for line in arch:
        line = line.strip()
        words.append(line)

    arch.close()

    number = random.randrange(0,len(words))
    secret_word = words[number].upper()

    correct_letters = ["_" for letter in secret_word]

    lost = False
    win = False
    erros = 0

    #print(secret_word)

    while(not lost and not win):

        tempt = input("Choose the letter? ")
        tempt = tempt.strip().upper()

        if(tempt in secret_word):
            index = 0
            for letter in secret_word:
                if(tempt == letter):
                    correct_letters[index] = letter
                index += 1
        else:
            erros += 1

        lost = erros == 6
        win = "_" not in correct_letters
        print(correct_letters)


    if(win):
        print("You WIN!!")
    else:
        print("You LOST!!")
    print("END GAME!!!!", f'The secret word is: {secret_word}')


if(__name__ == "__main__"):
    play()

