#this is a program to check if a number is even or odd without using 
# the modulo operator
num = int(input("Enter a number: "))
if (num & 1) == 0:
    print("entered number is even")
else:
    print("entered number is odd")