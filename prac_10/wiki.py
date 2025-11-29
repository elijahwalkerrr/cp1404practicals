import wikipedia

def main():
    while True:
        title = input("Enter page title: ")
        if title == "":
            print("Thank you.")
            break
        try:
            page = wikipedia.page(title, auto_suggest= False)
            print(page.title)
            print(page.summary)
            print(page.url)




