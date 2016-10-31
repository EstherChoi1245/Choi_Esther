number = input("Enter a number:")
sum = 0
num=number
def sumDigits():
    while num>0:
        sum += 1
        num = int(num/10)
    
print ("The sum of the digits of", number, "is", sumDigits())









