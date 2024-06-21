



import pyodbc
import os
from Hangman import *
from Word_Source import *


#dr = pyodbc.drivers()
#print(f'THIS IS MY DRIVER --- {dr}')

SERVER = ""
DATABASE = ""
USERNAME = ""
PASSWORD = ""



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
