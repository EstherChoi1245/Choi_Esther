number = int(input("Enter a number:"))

def getReverse():
    global rev
    rev = 0
    num = number
    while num > 0:
        rev = ((rev * 10)+(num % 10))
        num = int(num/10)
        
print (number, "reversed is", rev)









    
