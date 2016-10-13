height= int(input("How tall are you in inches?"))
weight= int(input("How much do you weigh in pounds?"))

bmi = 0
condition = 0

def calcBMI (num1):
    global bmi, condition
    bmi = ((weight*703)/(height**2))
    
    if bmi<18.5:
        condition = "underweight"
            return condition
    elif bmi<24.9:
        condition= "normal"
            return condition
    elif bmi<29.9:
        condition = "overweight"
            return condition
    elif bmi<34.9:
        condition = "obese"
            return condition
    elif bmi<39.9:
        condition = "very obese"
            return condition
    else:
        condition = "morbidly obese"
            return condition
        

print ("Your BMI is:", 
print ("You are", calcBMI(condition))


    

