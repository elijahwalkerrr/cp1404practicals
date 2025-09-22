name = input("Name: ")
print ("(H)ello\n(G)oodbye\n(Q)uit")
selection = input("Select Input: ")

while selection != 'Q':
    if selection == 'H':
        print(f"Hello {name}!")
        print("(H)ello\n(G)oodbye\n(Q)uit")
        selection = input("Select Input: ")
    elif selection == 'G':
        print(f"Goodbye {name}")
        print("(H)ello\n(G)oodbye\n(Q)uit")
        selection = input("Select Input: ")
    else:
        print("Invalid Response")
        print("(H)ello\n(G)oodbye\n(Q)uit")
        selection = input("Select Input: ")
print("Finished")

