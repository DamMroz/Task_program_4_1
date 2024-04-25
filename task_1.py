import string
from string import punctuation

def palindrome_check(word):
    trans = str.maketrans('', '', string.punctuation)
    new_word=word.translate(trans).translate \
   ({ord(c): None for c in  string.whitespace})
    return new_word[::-1].casefold() == new_word.casefold()
    
print(palindrome_check("Kajak"))