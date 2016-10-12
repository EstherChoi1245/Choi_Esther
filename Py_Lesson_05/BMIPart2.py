height= int(input("How tall are you in inches?"))
weight= int(input("How much do you weigh in pounds?"))

bmi = 0
condition = 0

def calcBMI (num1):
    global bmi, condition
    bmi = ((weight*703)/(height**2))
    return bmi
    if bmi<18.5:
        condition = "Underweight"
        return condition
    elif bmi<24.9:
        condition= "Normal"
        return condition
    elif bmi<29.9:
        condition = "Overweight"
        return condition
    elif bmi<34.9:
        condition = "Obese"
        return condition
    elif bmi<39.9:
        condition = "Very Obese"
        return condition
    else:
        condition = "Morbidly Obese"
        return condition
        

print ("Your BMI is:", bmi)
print ("You are", condition)


    
