side = float(input("What is the cube's side?"))

def calcSurf (side):
    return ((side**2)*6)
def printf (side):
    print ("The surface area of a cube with side",side,"is", (calcSurf(side)))
calcSurf (side)
printf (side)

