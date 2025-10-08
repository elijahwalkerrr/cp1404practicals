import statistics
from operator import truediv


def main():
   numbers = get_numbers()
   print_math(numbers)
   password = input("What Is Password: ")
   logic = password_checker(password)
   if logic:
       print("Cracked it")
   else:
       print("Wrooong")


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

def password_checker(password):
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    if password in usernames:
        return True
    else:
        return False
main()


