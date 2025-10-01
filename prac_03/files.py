# 1. Write code that asks the user for their name, then opens a file
# called name.txt and writes that name to it. Use open and close for this question.
name = input("What is Your Name?: ")
name_file = open("name.txt", "w")
print(name, file = name_file)
name_file.close()

#2
read_file = open("name.txt")
for line in read_file:
    print(f"Hi {line.strip()}, how are you???")
read_file.close()

#3.
number_read_file = open("numbers.txt","r")
first_line = int(number_read_file.readline())
second_line =int(number_read_file.readline())
result = first_line + second_line
print(result)
#4.
total_number_read_file = open("numbers.txt","r")
total = 0
for number_line in total_number_read_file:
    total += int(number_line)
print(total)