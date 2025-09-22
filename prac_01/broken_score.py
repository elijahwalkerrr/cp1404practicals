"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# User Enters Score
score = float(input("Enter score: "))
# Check score is valid and tell score status
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
