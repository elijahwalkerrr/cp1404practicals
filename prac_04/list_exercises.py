import statistics

def main():
   numbers = get_numbers()
   print_math(numbers)


def get_numbers():
    numbers = []
    for i in range (1,6):
        numbers.append(int(input(f"Number {i}: ")))
    return numbers

def print_math(numbers:list[list]):
    print (f"First:{numbers[0]}")
    print(f"Last:{numbers[-1]}")
    print(f"Minimum:{min(numbers)}")
    print(f"Maximum:{max(numbers)}")
    print(f"Average:{statistics.mean(numbers)}")

main()


