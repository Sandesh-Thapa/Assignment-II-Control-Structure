# Create a function, is_palindrome, to determine if a supplied word is the same if the letters are reversed.

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

string = input("Enter String to check palindrome: ")

print(is_palindrome(string))