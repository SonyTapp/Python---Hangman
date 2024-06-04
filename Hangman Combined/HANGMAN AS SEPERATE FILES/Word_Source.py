
import os
from Hangman import *
from Word_Source import *
from functions_CSV import *
from functions_List import *
from functions_SQL import *
from functions_Web_S import *

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