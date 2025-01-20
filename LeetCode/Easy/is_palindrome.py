import re

def is_palindrome(str):
    str = re.sub("[^a-zA-Z0-9]", "", str)
    str = str.replace(" ", "")
    if str.lower() == str[::-1].lower():
        return True
    else:
        return False
    

print(is_palindrome("A man, a plan, a canal: Panama"))

print(is_palindrome("race a car"))
