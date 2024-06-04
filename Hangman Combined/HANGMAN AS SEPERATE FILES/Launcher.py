
from Hangman import *
from Word_Source import *
from functions_CSV import *
from functions_List import *
from functions_SQL import *
from functions_Web_S import *

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