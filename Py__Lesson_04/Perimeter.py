length = float(input("What is the length of the rectangle?"))
width = float(input("What is the width of the rectangle?"))
perimeter = 2*(length+width)
def calcPerim (length, width):
    return (2*(length+width))

def printf (length, width):
    print ("Your rectangle is" ,calcPerim(length, width), "sq ft around.")

calcPerim (length, width)
printf (length, width)

