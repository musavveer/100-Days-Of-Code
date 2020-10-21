import wikipedia
import webbrowser

def get_info():
    wiki_select_page = wikipedia.random(1)
    
    wiki_store = wikipedia.page(wiki_select_page)

    user_choice = input("Would you like to read about {}. (Y/N): ".format(wiki_select_page)).lower().strip()

    if(user_choice == "y" or user_choice == "yes"):
        print("***Summary***"  )
        print(wiki_store.summary)
        wiki_open = input("Open Wiki page in browser? (Y/N)").lower().strip()
        if(wiki_open == "yes" or wiki_open == "y"):
            webbrowser.open(wiki_store.url,new=2)
        else:
            get_info()
        exit(0)
    elif(user_choice == "q" or user_choice == "quit"):
        exit(0)
    else:
        get_info()

if __name__ == "__main__":
    get_info()