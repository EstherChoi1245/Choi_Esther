
number = int(input("Enter a number:"))

def sumDigits():
    global digits, average
    Numsum = 0
    digits = 0
    average = 0
    num = number
    while num > 0:
        Numsum+= (num %10)
        digits+=1
        average = (Numsum/(len(str(number))))
        num = int(num/10)
        
sumDigits()

print ("The sum of the digits of", number, "is", average)

