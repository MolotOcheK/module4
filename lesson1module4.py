def is_palindrome(str):
    for i in range(len(str)):
        if(str[i] != str[-i - 1]):
            return False
    return True

print(is_palindrome("madam"))