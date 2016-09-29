r = float(input("What is the radius of the circle?"))
def calcArea (num1):
    return ((num1**2)*3.1415)
def formatf (num1):
    print ("The area of a circle with a radius of",r, "is {:10.5f}".format(calcArea(num1)))
    return (num1)
formatf (r)


