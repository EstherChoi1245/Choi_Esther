class Car:
    def __init__(self, p="", i="", e="", t=""):
        self.p= paint
        self.i= interior
        self.e= engines 
        self.t= tires

    def setCustom(self, p, i, e, t):
        paint = setCustom(paint)
        interior = setCustom(interior)
        engines = setCustom(engines)
        tires = setCustom(tires)
        
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
    
    paint = input("Enter a paint color:")
    interior = input("Enter an interior type:")
    engines = input("Enter an engine type:")
    tires = input("Enter tires:")

    car = Car(p, i, e, t)

    print ("Your vehicle is ready.....")
    print ("Paint:", car.getPaint(), "/n")
    print ("Interior:", car.getInterior(), "/n")
    print ("Engine:", car.Engines(), "/n")
    print ("Tires:", car.Tires(), "/n")
    print ("")
    
main()

    
