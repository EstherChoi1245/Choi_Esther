def thing(number):
    return (number/1728)

height = float(input("What is the height of the box in inches?"))
weight = float(input("What is the weight of the box in inches?"))
length = float(input("What is the length of the box in inches?"))
calcVol = height * weight * length


print ("The subwoofer box has a volume of", (thing(calcVol)), "cubic feet.")

