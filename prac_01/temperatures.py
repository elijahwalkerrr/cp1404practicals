"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
# User Inputs temperature to be altered to either Fahrenheit or Celsius
# Print Menu
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
# Obtain User Input
choice = input(">>> ").upper()
# Determine if Correct was Correct and Process Input
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"Result: {celsius:.2f} C")
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")