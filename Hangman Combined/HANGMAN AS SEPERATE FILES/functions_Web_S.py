
import os
from Hangman import *
from Word_Source import *
import requests 
from bs4 import BeautifulSoup


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