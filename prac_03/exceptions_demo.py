"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When anything except an integer is entered.
2. When will a ZeroDivisionError occur?
When 0 is entered as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, adding an if statement to check if the number was zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print ("Denominator cannot be zero")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")