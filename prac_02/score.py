"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random



def main ():
    score = float(input("Enter score: "))
    status = score_status(score)
    print(status)
    random_score = random.randint(0,100)
    random_status = score_status(random_score)
    print(f"A random score is {random_score}, that is {random_status}!")


def score_status (score):
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

main()