item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price for item 1:"))
item2 = input("Please enter item 2:")
price2 = float(input("Please enter the price for item 2:"))
item3 = input("Please enter item 3:")
price3 = float(input("Please enter the price for item 3:"))
item4 = input("Please enter item 4:")
price4 = float(input("Please enter the price for item 4:"))

subtotal = price1+price2+price3+price4

if subtotal>=2000: 
    discount = subtotal*0.85
if subtotal<2000:
    discount = subtotal*1
def formatf (num1, num2):
    print ("{:^10}\t{:5.2}".format(num1, num2))
def formatg (num5):
    print ("{:<5}\t{:4.4}".format(num5))       
formatf(item1, price1)
formatf(item2, price2)
formatf(item3, price3)
formatf(item4, price4)
print ("<<<<<<<<<<<< Receipt >>>>>>>>>>>>>>") 
print ("Subtotal:" ,formatg(subtotal))
print ("Tax:", formatg(subtotal*0.08))
print ("Discount:",formatg(discount))
print ("Total:", formatg(discount + (subtotal*0.08)))
print ("___________________________")
print ("Thank you!")



    
