number = int(input("Enter a number:"))

def sumDigits():
    global summ
    summ = 0
    num = number
    while num > 0:
        summ = summ + (num % 10)
        num = int(num/10)

sumDigits()

print ("The sum of the digits of", number, "is", summ)









