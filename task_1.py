def palindrome_check(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome_check("enter word here"))