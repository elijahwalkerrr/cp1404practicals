import random
# Write a complete Python program following the standard structure that uses a main and other functions.
# Use a main menu following the standard menu pattern.
#
# The menu should have four separate options:
#
# (G)et a valid score (must be 0-100 inclusive)
# (P)rint result (copy or import your function to determine the result from score.py)
# (S)how stars (this should print as many stars as the score)
# (Q)uit
# Handle each of these (except quit) separately, and consider how you can reuse your functions.
#
# In main(), before the menu loop, get a valid score using your function.
# When the user quits, say some kind of "farewell".

def main():
    valid = False
    menu_selection = input("PICK")
    while menu_selection != "Q":
        if menu_selection == "G":
            score,valid = get_valid_input()
            menu_selection = input("PICK")
        elif menu_selection == "P":
            if valid == 0:
                score, valid = get_valid_input()
                print_result(score)
                menu_selection = input("PICK")
            else:
                print_result(score)
                menu_selection = input("PICK")
        elif menu_selection == "S":
            if valid == 0:
                score, valid = get_valid_input()
                score_stars(score)
                menu_selection = input("PICK")
            else:
                score_stars(score)
                menu_selection = input("PICK")
        else:
            print ("Invalid Input")
            menu_selection = input("PICK")
    print("Farewell")


















def get_valid_input ():
    score = int(input("Score: "))
    if score < 0 or score > 100:
        print("Invalid Score")
        score = 0
        valid = False
        return score, valid
    else:
        print("Valid Score")
        valid = True
        return score, valid


def print_result (score):
    if score < 0 or score > 100:
        status = "Invalid score"
        return status
    elif score >= 90:
        status = "Excellent"
        return status
    elif score >= 50:
        status = "Passable"
        return status
    else:
        status ="Bad"
        return status
def score_stars (score):
    print("*"* score)

main()