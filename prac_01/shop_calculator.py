# Calculate the Prices of Different Items
# Input Number of item
number_of_items = int(input("Number of items: "))
if number_of_items <= 0:
    print("Invalid Number of items")
    number_of_items = int(input("Number of items: "))
    for i in range (0,number_of_items,1):
        item_price = int(input("Price of Items: $"))
        if i<=0:
            total_cost = item_price
        else:
            total_cost = total_cost + item_price

    print(f"Total Price for {number_of_items} items is ${total_cost}")
