#this is a program to check if a numer is a palindrome
num = int(input("Enter a number: "))
is_palindrome = True
temp = num
reversed_num = 0
while temp > 0:   
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp = temp // 10
if num == reversed_num:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")   