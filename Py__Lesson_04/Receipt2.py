def printf (item, price):
    print ("* {:>20} ........\t{:10.3}".format(item, price))

item1 = input("Please enter Item 1: ")
price1 = float(input("Please enter the price: "))

item2 = input("Please enter Item 2: ")
price2 = float(input("Please enter the price: "))

item3 = input("Please enter Item 3: ")
price3 = float(input("Please enter the price: "))
subtotal = price1 + price2 + price3
tax = (price1 + price2 + price3)*0.07
total = (price1 + price2 + price3)*1.07
print ("<<<<<<<<<<<<<<<__Recipt__>>>>>>>>>>>>>>>")
printf (item1, price1)
printf (item2, price2)
printf (item3, price3)
printf ("Subtotal:", subtotal)
printf ("Tax:", tax)
printf ("Total:", total)
print ("____________________________________")
print ("* Thank you for your support *")
