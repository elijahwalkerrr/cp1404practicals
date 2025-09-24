# Score Menu

def main():
    valid = False
    print ("(G)et a valid score (must be 0-100 inclusive)\n" +"(P)rint result\n" + "(S)how stars (this should print as many stars as the score)\n" + "(Q)uit")
    menu_selection = input("Select From Menu: ")
    while menu_selection != "Q":
        if menu_selection == "G":
            score,valid = get_valid_input()
            menu_selection = input("Select From Menu:")
        elif menu_selection == "P":
            if valid == 0:
                score, valid = get_valid_input()
                status = print_result(score)
                print(status)
                menu_selection = input("Select From Menu:")
            else:
                status = print_result(score)
                print(status)
                menu_selection = input("Select From Menu:")
        elif menu_selection == "S":
            if valid == 0:
                score, valid = get_valid_input()
                number_of_stars = score_stars(score)
                print(f"Wow! Your Score was this many stars: {number_of_stars}")
                menu_selection = input("Select From Menu:")
            else:
                number_of_stars = score_stars(score)
                print(f"Wow! Your Score was this many stars: {number_of_stars}" )
                menu_selection = input("Select From Menu:")
        else:
            print ("Invalid Input")
            menu_selection = input("Select From Menu:")
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
        status = "Bad"
        return status

def score_stars (score):
    number_of_stars = "*"*score
    return number_of_stars

main()