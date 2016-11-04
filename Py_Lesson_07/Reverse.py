number = int(input("Enter a number:"))

def getReverse():
    global Rev, num
    Rev = 0
    num = number
    while num > 0:
        Rev = ((Rev * 10)+(num % 10))
        num = int(num/10)

getReverse ()

print (number, "reversed is", Rev)









    
