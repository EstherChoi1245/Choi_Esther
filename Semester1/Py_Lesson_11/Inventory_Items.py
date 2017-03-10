import random
class InvIt:
    def __init__(self, manu, iname, iprice="", categ = ""):
        self.manufac = manu
        self.itemn = iname
        self.itemp = iprice
        self.category = categ
        self.userpc = random.randint(0, 10000000000)
        
    def setNames(self, manu, iname, iprice, categ):
        manu = setNames(manufac)
        iname = setNames(itemn)
        categ = setNames(category)
        iprice = setNames(itemp)
        userpc = setNames(userpc)
        
    def getmanu(self):
        return self.manufac
    def getitem(self):
        return self.itemn
    def getcate(self):
        return self.category
    def getprice(self):
        return self.itemp
    def getupc(self):
        return self.userpc
    def __str__(self):
        return "Customer Info... \nManufacturer: " + self.manufac + "\nItem Name: " + self.itemn + "\nCategory: " + self.category + "\nItem Price: " + self.itemp + "\nUser Price: " + str(self.userpc)
    
def main():
    manufac = input("Enter a manufacturer: ")
    itemn = input("Enter an item name: ")
    item1 = InvIt(manufac, itemn)
    ioj = input ("Would  you like to enter the price and category? (y or n): ")
    if ioj == "n":
        item1 = InvIt(manufac, itemn)
    else:
        category = input("What is the category? ")
        itemp = input("What is the price? ")
        item1 = InvIt(manufac, itemn, itemp, category)
    print(item1)
  
main()
