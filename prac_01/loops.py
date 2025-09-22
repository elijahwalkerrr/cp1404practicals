# Demonstration: All Odd numbers From 1-20
for i in range (1,21,2):
    print(i,end=' ')
print()

# A. Count in 10s from 0 to 100
for i in range (0, 101, 10):
    print(i,end=' ')
print()

#B. Count down from 20 to 1
for i in range (20,0,-1):
    print(i,end=' ')
print()

#C. Print A Number of Stars
number_of_stars = int(input("Enter the number of stars: "))
for i in range (0,number_of_stars, 1):
    print("*",end='')
print()

#D. Print Line of Increasing Stars
number_of_lines = int(input("Enter the lines of increasing stars: "))
for i in range (0,number_of_lines):
    print("*" * (i+1))
print()