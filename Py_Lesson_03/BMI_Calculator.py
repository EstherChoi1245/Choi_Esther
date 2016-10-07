print ("Hello. I will be finding your BMI.")

num = int (input("How tall are you in inches?"))
num2 = int (input("How much do you weigh in pounds?"))
calculation = 703 * (num2/(num**2))
print ("Your BMI is", calculation)

