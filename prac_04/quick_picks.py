import random

LINES = int(input("Number of Quick Picks Lines: "))
for i in range (LINES):
    numbers = []
    while len(numbers) < 6:
        numb = random.randint(1, 45)
        if numb in numbers:
            numb = random.randint(1, 45)
            numbers.append(numb)
        else:
            numbers.append(numb)
        numbers.sort()
    print (" ".join(f"{num:2}" for num in numbers))






