list_1=[]
list_2=[]
def palindrome(a):
    for element in a:
        list_1.append(element)
    for element2 in reversed(a):
        list_2.append(element2)
    
def fun():
    if list_1==list_2:
        return True
    else:
        return False
    
palindrome("enter word here")

print(fun())