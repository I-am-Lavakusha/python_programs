#palindrom program without using slicing
string = input("Enter a string: ")
is_palindrome = True
length = len(string)
for i in range(length // 2):
    if string[i] != string[length - 1 - i]:
        is_palindrome = False
        break
if is_palindrome:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")