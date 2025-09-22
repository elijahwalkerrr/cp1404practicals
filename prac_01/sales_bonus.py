"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter the sales: $"))

while sales >= 0:
    if sales >= 1000:
        percent_bonus = 0.15
    else:
        percent_bonus = 0.10

    bonus = sales * percent_bonus
    print(f"Your Bonus is ${bonus}")
    sales = float(input("Enter the sales: $"))





