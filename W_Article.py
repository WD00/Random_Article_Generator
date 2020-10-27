import webbrowser, wikipedia

def get_article_page():
    page_wikipedia = wikipedia.random(1)

    loading_wikipedia = wikipedia.page(page_wikipedia)

    choice = input("Do you want more info about {} (Y/N/Q)".format(page_wikipedia)).lower().strip()

    if (choice == "y" or choice == "yes"):
        print ("\n")
        print (loading_wikipedia.summary)
        wikiopen = input("\n Would you like to read the whole article? (Y/N)").lower().strip()
        if(wikiopen == "yes" or wikiopen == "y"):
            webbrowser.open(loading_wikipedia.url, new = 2)
        else:
            get_article_page()
        exit(0)
    elif(choice == "q" or choice == "quit"):
        exit(0)
    else:
        get_article_page()

if __name__ == "__main__":
    get_article_page()