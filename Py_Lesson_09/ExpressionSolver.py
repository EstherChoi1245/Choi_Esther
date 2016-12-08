expression= input("Please enter a mathematical expression with spaces between terms:")
equation = expression.split(" ")

i=0
while i < len(equation):
    if i <len(equation) and equation[i] == "*" or "/":
        if equation[i]== "*":
            equation[i]=int(equation[i-1])*int(equation[i+1])
            equation.pop(i+1)
            equation.pop(i-1)
        elif equation[i]== "/":
            equation[i]= int(equation[i-1])/(int(equation[i+1]))
            equation.pop(i+1)
            equation.pop(i-1)        
    i+= 1
                    

i=0
while i < len(equation):
    if i <len(equation) and (equation[i]== "+" or "-"):
        if equation[i]== "+":
            equation[i]=int(equation[i-1])+int(equation[i+1])
            equation.pop(i-1)
            equation.pop(i)
        elif equation[i]== "-":
            equation[i]= int(equation[i-1])-(int(equation[i+1]))
            equation.pop(i-1)
            equation.pop(i)        
    i+= 1
                    
print(equation)


    



