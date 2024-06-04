
#---------------------------------

import random
import time
import os

#-------------------------------

from functions_List import *
from functions_CSV import*
from functions_SQL import *
from functions_Web_S import *
from Word_Source import *

# ---------- GAME STARTS ---------------

def game():
    #Randomly choose a word from the list 
    global secret 
    secret = random.choice(words)
    secret = secret.upper()
    guessed = ''
    turns = 7
    placed = '_' * len(secret)
    l = list(placed)
    done = 0

    while turns:
        while True:
            os.system("clear")
            hang(turns)
            print("\n\nSecret Word....:", ' '.join(l))
            print("\n\nLetters Used....:",guessed)
            print("\n\nTries to go.....:",turns)
            typed = input("\n\nGuess a Letter......: ").upper() # I ADDED UPPER BC IT WAS ANNOYING ME
            if typed not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or len(typed) >1:
                input ("Single Upper Case Letter ONLY! Press ENTER to continue......")
            else:
                break


# ---------- UNDERSSCORES ---------------

        turns = 7                               # sets turns to 7 at the start of the Loop
        if typed not in guessed:                # if typed letter isnt in the list of guessed letters  EG... s = selection  typed = D
            guessed = guessed + typed           # adds guessed letter 'typed' to the string og guessed letters  Round 1 - guessed = 'D'
            g = list(guessed)                   # turns guessed letters into a list        g = ['D']
            s = list (secret)                   # turns the secret word into a list        s = ['S','E',.......]

            for k in range (len(g)):            # iterates over all guessed letters each time a new one is added
                kstr= guessed [k]               # first iteration k=0 and the first guessed letter is assigned to kstr = D
                if kstr in s:                   # if the guessed letter is in the secret word(list) 
                    for i in range(len(s)):     # iterates over each letter in the secret word(list)
                        if kstr == s[i]:        # if the guessed letter = letter in secret word(list) iterating over each letter above 
                            l[i] = kstr         # The underscore at the same index in 'l' will be chagenged to the guessed letter
                else: 
                    turns = turns -1            # for every guessed letter not in the secret word, turns - 1
            

# ---------- WIN OR LOSE ---------------

            if l == s:
                os.system("clear")
                hang(turns)
                print("")
                print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗                   ██╗ ")
                print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║            ██╗    ╚██╗")
                print(" ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║            ╚═╝     ██║")
                print("  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║            ██╗     ██║")
                print("   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║            ╚═╝    ██╔╝")
                print("   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝                   ╚═╝ ")
                print("")
                input("Press ENTER to continue...")                     
                break 

            if turns == 0:
                os.system("clear")
                hang(turns)
                print("")
                print("▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ ")
                print(" ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌")
                print("  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌")
                print("  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌")
                print("  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ ")
                print("   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ ")
                print(" ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ ")
                print(" ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ ")
                print(" ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    ")
                print(" ░ ░                           ░                  ░      ")
                print("")
                input(f"THE WORD WAS -- {secret} --")
                input("Press ENTER to continue...")
                break


# ---------- SPLASH ----------------

def splash():
    os.system("clear")
    #Intro to Game
    delay = 3
    while delay:
        print('  ====================')
        print('  LET\'S PLAY HANGMAN')
        print('  ', delay, 'secs to start')
        print('  ====================\n\n')
        print('''
        _______
        |/    |
        |     O
        |   \_|_/
        |     |
        |    / \\
        |   /   \\
    ____|____                 
    \n''')
        print('  ====================')
        time.sleep(1)
        delay = delay - 1
        os.system("clear")

# ---------- GALLOWS ---------------

def hang(turn):
    if turn < 7:
        print('     _______     ')
        print('     |/    |     ')
    else:
        print('     _______     ')
        print('     |/          ')

    if turn < 6:
        print('     |     O     ')
    else:
        print('     |           ')  

    if turn < 5:
        print('     |   \_|_/     ')
    else:
        print('     |             ')        

    if turn < 4:
        print('     |     |       ')
    else:
        print('     |             ')  

    if turn < 3:
        print('     |    / \\     ')
    else:
        print('     |             ')  

    if turn < 2:
        print('     |   /   \\    ')
    else:
        print('     |             ')  

    print(' ____|_____')





