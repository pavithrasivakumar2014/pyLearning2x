
# Task1: Create a function that checks if a given string is a palindrome (reads the same forwards and backward)

string = input("Enter the string to check for palindrome: ")
if string == string[::-1]:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")