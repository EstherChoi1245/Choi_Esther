item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price for item 1:"))
item2 = input("Please enter item 2:")
price2 = float(input("Please enter the price for item 2:"))
item3 = input("Please enter item 3:")
price3 = float(input("Please enter the price for item 3:"))
item4 = input("Please enter item 4:")
price4 = float(input("Please enter the price for item 4:"))
subtotal = price1+price2+price3+price4


def formatf (num1, num2):
    print ("{:<10}{:0.2f}".format(num1, num2))

def discountc():
    global subtotal, discount
    if subtotal>=2000: 
        discount = subtotal*0.15
    else:
        discount = subtotal*0
        
        
discountc()
discount=0
tax=subtotal*0.08
total= subtotal-discount+tax

print ("<<<<<<<<<<<< Receipt >>>>>>>>>>>>>>")
formatf(item1, price1)
formatf(item2, price2)
formatf(item3, price3)
formatf(item4, price4)

print (formatf("Subtotal:", subtotal))
print (formatf("Discount:",discount))
print (formatf("Tax:",tax))
print (formatf("Total:", total))
print ("___________________________")
print ("Thank you!")



    
