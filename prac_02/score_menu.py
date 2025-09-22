import random

def main():
    menu = """(G)et a valid score (must be 0-100 inclusive)
    (P)rint result (copy or import your function to determine the result from score.py)
    (S)how stars (this should print as many stars as the score)
    (Q)uit"""
    print(menu)
    selection = input("Select Input")
    while selection != "Q":
        if selection == "G":



def get_valid_score():
    score = input(int("Get Valid Input: "))
    while score < 0 or score > 100:
        score = input(int("Get Valid Input: "))
    return score

def print_result(score):
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

def show_stars()
    print()