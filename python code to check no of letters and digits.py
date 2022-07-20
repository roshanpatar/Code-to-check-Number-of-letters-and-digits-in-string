string = input("enter the string to check number of alphabets and digits:")
letters = digits = 0
for i in range(len(string)):
    if(string[i].isalpha()):
        letters = letters + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    
        
print("\n LETTERS:", letters)
print(" DIGITS:", digits)

