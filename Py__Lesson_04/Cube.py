#first program without global variable
side = float(input("What is the cube's side?"))

def calcSurf (side):
    return ((side**2)*6)
def printf (side):
    print ("The surface area of a cube with side",side,"is {:10.5f}".format(calcSurf(side)))
calcSurf (side)
printf (side)




#second program with global variable and rectangular prism
side = float(input("What is the rectangle's side?"))
side1 = float(input("What is the rectangle's other side?"))
side2 = float(input("What is the rectangle's last side?"))
sa = 0

def calcSurf (num1, num2, num3):
    global side, side1, side2

def printf (num1, num2, num3):
    global sa
    sa = ((2*(side*side1))+(2*(side1*side2))+(2*(side*side2)))
    
calcSurf (side, side1, side2)
printf (side, side1, side2)
print ("The surface area of a cube with side",side, "is",(sa))
