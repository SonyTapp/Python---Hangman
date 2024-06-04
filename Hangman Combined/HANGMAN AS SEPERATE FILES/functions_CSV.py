
import os
from Hangman import *
from Word_Source import *



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