import math
class Distance:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        distance = 0
        
    def setValues(self, x1, y1, x2, y2):
        x1 = setValues(x1)
        y1 = setValues(y1)
        x2 = setValues(x2)
        y2 = setValues(y2)

    def getMPH(self):
        distance = math.sqrt(((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne)));
        return distance


def main():
    x1= int(input("Enter an x-coordinate:"))
    y1= int(input("Enter an y-coordinate:"))
    x2= int(input("Enter another x-coordinate:"))
    y2= int(input("Enter another y-coordinate:"))
    
    distance = Distance(x1, y1, x2, y2)  

    print ("The distance between (", x1, ",", y2, ") and (", x2, ",", y2 ,") is", distance.getMPH())


main()
