class Car:
    def __init__(self, p="", i="", e="", t=""):
        self.paint= p
        self.interior= i
        self.engines= e 
        self.tires= t

    def setCustom(self, p, i, e, t):
        paint = setCustom(p)
        interior = setCustom(i)
        engines = setCustom(e)
        tires = setCustom(t)
        
    def getPaint(self):
        return self.paint
    
    def getInterior(self):
        return self.interior

    def getEngines(self):
        return self.engines

    def getTires(self):
        return self.tires

def main():
    global p, i, e, t
    
    p = input("Enter a paint color:")
    i = input("Enter an interior type:")
    e = input("Enter an engine type:")
    t = input("Enter tires:")

    car = Car(p, i, e, t)

    print ("Your vehicle is ready.....")
    print ("Paint:", car.getPaint())
    print ("Interior:", car.getInterior())
    print ("Engine:", car.getEngines())
    print ("Tires:", car.getTires())
    print ("")

    
main()

    
