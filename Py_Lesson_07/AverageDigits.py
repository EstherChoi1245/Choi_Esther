number = int(input("Enter a number:"))
digits = 0
average = 0

def avDigits ():
    global digits, average 
    num = number
    while num>0:
        digits+=1
        num = int(num/10)
        average = (num + digits)/num
        

avDigits()
print ("The average of the digits in", number, "is", average)








    
