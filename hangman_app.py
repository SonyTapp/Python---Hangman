



# ---------- SECTION 1 ---------------


import random
import time
import os

# . LIST OF WORDS

words = ['variable','string','integer','selection','iteration','loop','operator']
#words = ['']


# ---------- SECTION 1 END -----------



# ---------- SECTION 6 ---------------

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

# ---------- SECTION 6 END ------------



# ---------- SECTION 7 ---------------
        #STILL WHILE TRUE - INFINITE

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
            

# ---------- SECTION 7 END ------------



# ---------- SECTION 8 ---------------

            if l == s:
                os.system("clear")
                hang(turns)
                print()
                print()
                print()
                input("Press ENTER to continue...")
                break 

            if turns == 0:
                os.system("clear")
                hang(turns)
                print()
                print()
                print()
                input("Press ENTER to continue...")
                break

# ---------- SECTION 8 END ------------



# ---------- SECTION 2 ----------------

def main():
    os.system("clear")
    print("=====================")
    print("WELCOME TO HANGMAN")
    print("=====================")
    print("     Main Menu\n\n")
    print(" 1) Play Game")
    print(" 2) Add New Word")
    print(" 3) Exit\n\n")
    print("=====================")
    Choice = input('Input an Option: ')
    if Choice == "1":
        splash()
        game()
    elif Choice == "2":
        Add_word()
    elif Choice == "3":
        os._exit(0)
    else:
        input("Please Input Valid Option")
    main()                

# ---------- SECTION 2 END ------------



# ---------- SECTION 5 ---------------

def Add_word():
    os.system("clear")
    print("Old word list: ", ", ".join(words))
    New_word = input('Input New Word: ')
    if len(New_word) > 0:
        words.append(New_word)
    os.system("clear")
    print("New word list:", ", ".join(words)) 
    input("Press ENTER to Continue...")

# ---------- SECTION 5 END ------------



# ---------- SECTION 3 ----------------
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

# ---------- SECTION 3 END ------------




# ---------- SECTION 4 ---------------

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

if __name__ == '__main__':
    main()                

    
# ---------- SECTION 4 END ------------










