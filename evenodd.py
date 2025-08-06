#this program checks if a number is even or odd. if it is greater than 0

num = int(input("Enter a number: "))
if (num > 0):
    if (num & 1) == 0:
        print("entered number is even")
    else:
        print("entered number is odd")
else:
    print("Please enter a positive number")