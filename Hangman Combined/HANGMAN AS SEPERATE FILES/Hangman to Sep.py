#  WORDS LIST --- biscuit,caramel,diamond,emerald,giraffe,harvest,journey,library,mystery,octopus,penguin,quartz,rocket,sapphire,turmoil,unicorn,violet,whisper,yogurt,zodiac

# ---------- SECTION 1 IMPORTS ---------------   TO_DO --- Error handles, screen clears, improve add and delete display, choose to add another word or more comma seperated or both 
                                                #CSV ALSO DOESNT UPDATE WORDS AFTER ADD

import random
import time
import os
import requests 
from bs4 import BeautifulSoup

#--------INSERT CONNECTION STRING TO ASP--------------

import pyodbc


#dr = pyodbc.drivers()
#print(f'THIS IS MY DRIVER --- {dr}')

SERVER = "
DATABASE = "
USERNAME = "dn"
PASSWORD = "a"



connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)

cursor = conn.cursor()
cursor.execute("SELECT word FROM tWords")

records = cursor.fetchall()

sql_words = []

for r in records:
    rec = []
    for col in r:
        rec.append(col)
        #words.extend(rec)                      # Both of these work
        sql_words = sql_words + rec             # Both of these work

    #print(sql_words)

   

#--------END CONNECTION STRING TO ASP--------------

# ---------- FUNCTIONS FOR PYTHON LIST -------------------

list_words = ['variable','string','integer','selection','iteration','loop','operator']  # THE LIST


def list_add_word():
    os.system("clear")
    print("Old word list: ", ", ".join(list_words))
    New_word = input('Input New Word: ')
    if len(New_word) > 0:
        list_words.append(New_word)
    os.system("clear")
    print("New word list:", ", ".join(list_words)) 
    input("Press ENTER to Continue...")



def list_delete_word():
    os.system("clear")
    print("Old word list: ", ", ".join(list_words))
    del_word = input('Input Word to Delete: ') 
    if del_word in list_words:
        list_words.remove(del_word)
        os.system("clear")
        print("New word list:", ", ".join(list_words)) 
        input("Press ENTER to Continue...") 
    else:
       print('That is not in the list!')     



def list_show():
    os.system("clear")
    print(list_words)
    input("Press ENTER to continue...")



#  Python List Main Menu

def list_main():
    os.system("clear")
    print("=====================")
    print("WELCOME TO HANGMAN")
    print("=====================")
    print("     Main Menu - List \n\n")
    print(" 1) Play Game")
    print(" 2) Show words")
    print(" 3) Add New Word")
    print(" 4) Delete Word")
    print(" 5) Switch Word Source")
    print(" 6) Exit\n\n")
    print("=====================")
    Choice = input('Input an Option: ')
    if Choice == "1":
        splash()
        game()
    elif Choice == "2":
        list_show()
    elif Choice == "3":
        list_add_word()
    elif Choice == "4":
        list_delete_word()  
    elif Choice == "5":
        source_words()
        return 
    elif Choice == "6":
        os._exit(0)
            
    else:
        input("Please Input Valid Option")
    list_main()   


# ---------- Python List END -------------------

# ---------- FUNCTIONS FOR CSV -------------------

csv_words = []

def csv_read():    # ** READS CSV TO LIST **
    os.system("clear")
    file = open("words.csv","r") 
    csv_words.clear()
    for word in file:
        csv_words.append(word.strip("\n"))
    file.close()
    print(csv_words) 

def csv_show():    # ** READS CSV TO LIST **
    os.system("clear")
    file = open("words.csv","r") 
    csv_words.clear()
    for word in file:
        csv_words.append(word.strip("\n"))
    file.close()
    os.system("clear")
    print(csv_words) 
    input("Press ENTER to continue...")


def csv_add_word():
    os.system("clear")
    csv_read()
    userInput = input('Enter words seperated by a commma: ').replace(" ","")
    userList = userInput.split(",")
    file = open("words.csv", "a")              # REPLACED 'w' FOR WRITE, WITH 'a' FOR APPENDvto update the 
    for word in userList:                        
        file.write(word+'\n')  
        csv_words.append(word)  
    file.close  
    os.system("clear")
    print(csv_words)
    input("Press ENTER to continue...")
    

def csv_delete_word():
    os.system("clear")
    csv_read()
    userInput = input("Enter word to Delete: ").replace(" ","")  

    #------- write to file ------

    file = open("words.csv","r")     # READS CSV BEFORE DELETION FOR UP TO DATE WORDS -- I think -- but i dont think it is needed, unless magbe you just added a word  ---- WHAT DOES THIS DO
    words = []
    for word in file:
        words.append(word.strip("\n"))
    file.close()    

    #------- write to file ------
    file = open("words.csv","w")
    for word in words:
        if word != userInput:
            file.write(word+'\n')

    file = open("words.csv","r")     # READS CSV BEFORE DELETION FOR UP TO DATE WORDS -- I think -- but i dont think it is needed, unless magbe you just added a word
    words = []
    for word in file:
        words.append(word.strip("\n"))
    file.close()           

    os.system("clear")
    csv_show()        


def create_csv_list():
    userInput = input('Enter words seperated by a commma: ').replace(" ","")    
    userList = userInput.split(",")
    file = open("words.csv", "w")
    for word in userList:                             
        file.write(word+'\n')
    file.close    

#  CSV Main Menu

def csv_main():
    global source_words
    os.system("clear")
    print("=====================")
    print("WELCOME TO HANGMAN")
    print("=====================")
    print("     Main Menu - CSV \n\n")
    print(" 1) Play Game")
    print(" 2) Show words")
    print(" 3) Add New Word")
    print(" 4) Delete Word")
    print(" 5) Create New List")
    print(" 6) Switch Word Source")
    print(" 7) Exit\n\n")
    print("=====================")
    Choice = input('Input an Option: ')
    if Choice == "1":
        splash()
        game()
    elif Choice == "2":
        csv_show()
    elif Choice == "3":
        csv_add_word()
    elif Choice == "4":
        csv_delete_word()  
    elif Choice == "5":
        create_csv_list()  
    elif Choice == "6":
        source_words()  
        return      
    elif Choice == "7":
        os._exit(0)
    else:
        input("Please Input Valid Option")
    csv_main()   


# ---------- CSV FUNCTIONS END -------------------

# ---------- SQL FUNCTIONS -----------------------

def sql_show_words():
    cursor.execute("SELECT * FROM tWords")
    show_all = cursor.fetchall()
    print(show_all)
    input("Press ENTER to Continue...")

def sql_del_word():
    cursor.execute("SELECT * FROM tWords")
    show_all = cursor.fetchall()
    print(show_all)
    del_key = int(input('input delete key: '))
    #cursor.execute("DELETE FROM tWords WHERE WordID = (%s)", (del_key,))  
    cursor.execute("DELETE FROM tWords WHERE WordID = (?)", (del_key,))
    conn.commit()

def sql_add_word():
    os.system("clear")
    sql_show_words()
    New_word = input('Input New Word: ')
    if len(New_word) > 0:
        cursor.execute("INSERT INTO tWords (Word) VALUES (?)", (New_word,))
        conn.commit()
        sql_words.append(New_word)
    
    os.system("clear")
    print("New word list:", ", ".join(sql_words)) # this is what was there before
    #print("New word list:",words) 
    input("Press ENTER to Continue...")


    #  Python List Main Menu

def sql_main():
    os.system("clear")
    print("=====================")
    print("WELCOME TO HANGMAN")
    print("=====================")
    print("     Main Menu - SQL\n\n")
    print(" 1) Play Game")
    print(" 2) Show Words")
    print(" 3) Add Words")
    print(" 4) Delete Word")
    print(" 5) Switch Word Source")
    print(" 6) Exit\n\n")
    print("=====================")
    Choice = input('Input an Option: ')
    if Choice == "1":
        splash()
        game()
    elif Choice == "2":
        sql_show_words()
    elif Choice == "3":
        sql_add_word() 
    elif Choice == "4":
        sql_del_word()  
    elif Choice == "5":
        source_words()
        return     
    elif Choice == "6":  
        os._exit(0)
        
    else:
        input("Please Input Valid Option: ")
    sql_main()             

# ---------- SQL FUNCTIONS END -------------------

# ---------- WEBS FUNCTIONS ----------------------

#   COLLECT WORDS FROM WEBPAGE 
  
url = 'https://sonytapp.github.io/Portfolio/word_list.html'

response = requests.get(url)
response = response.content
soup = BeautifulSoup(response, 'html.parser')

ol = soup.find('ol')          # Finds the first ordered list
web_words_collect = ol.find_all('li')     # makes a list of all the 'li' tags in the ol
web_words = []
#print(words)

for tag in web_words_collect:
    #tagContent = tag.find('value')
    #word = tag.attrs['value']
    get_word = tag.text 
    web_words.append(get_word)

    #   FUNCTIONS

def web_add_word():
    os.system("clear")
    print("Old word list: ", ", ".join(web_words))
    New_word = input('Input New Word: ')
    if len(New_word) > 0:
        web_words.append(New_word)
    os.system("clear")
    print("New word list:", ", ".join(web_words)) 
    input("Press ENTER to Continue...")    


def web_show():
    print(web_words)
    input("Press ENTER to continue...") 


#  Web Main Menu 

def web_main():
    os.system("clear")
    print("=====================")
    print("WELCOME TO HANGMAN")
    print("=====================")
    print("     Main Menu - Web\n\n")
    print(" 1) Play Game")
    print(" 2) Show Words")
    print(" 3) Add New Word")
    print(" 4) Switch Word Source")
    print(" 5) Exit\n\n")
    print("=====================")
    Choice = input('Input an Option: ')
    if Choice == "1":
        splash()
        game()
    elif Choice == "2":
        web_show()
    elif Choice == "3":
        web_add_word()
    elif Choice == "4":
        source_words()  
        return       
    elif Choice == "5":
        os._exit(0)    
    else:
        input("Please Input Valid Option")
    web_main()  


# ---------- WEBS FUNCTIONS END ------------------
    
    

# ----------PRE GAME CHOICE OF WORDS ---------------

menu_type = ''

def source_words():
    global words
    global menu_type
    os.system("clear")
    print("=============================")
    print("CHOOSE YOUR SOURCE OF WORDS")
    print("=============================")
    print("\n")
    print(" 1) Python List")
    print(" 2) SQL DATABASE")
    print(" 3) CSV File")
    print(" 4) Web Scraping")
    print(" 5) Exit\n\n")
    print("=====================")
    Choice = input('Input an Option: ')
    if Choice == "1":
        words = list_words
        menu_type = 'list'
        list_main()        
    elif Choice == "2":
        words = sql_words
        menu_type = 'sql' 
        sql_main() 
    elif Choice == "3":
        words = csv_words
        menu_type = 'csv' 
        csv_main() 
    elif Choice == "4":
        menu_type = 'web'  
        words = web_words
        web_main()
    elif Choice == "5":
        os._exit(0)
    else:
        input("Please Input Valid Option")
        source_words()                

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


# ---------- EXECUTE GAME ------------

if __name__ == '__main__':
    source_words()
    if menu_type == 'list':
        list_main() 
    elif menu_type == 'sql':
        sql_main()
    elif menu_type == 'csv':
        csv_main()    
    elif menu_type == 'web':
        web_main()                  

# ---------- SECTION 4 END ------------










