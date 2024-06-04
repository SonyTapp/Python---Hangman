
import os
from Hangman import *
from Word_Source import *

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