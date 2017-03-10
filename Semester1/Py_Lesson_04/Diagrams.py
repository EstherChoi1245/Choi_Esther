num5 = int(input("Enter a number:"))
def function1 (num1):
     output = num1*2 #variable performs action but is not callable outside of function
     return output #return function returns output, the result
print ("Your number doubled is",(function1(num5))) #prints the result of putting variable num5 through function

#- Diagram:

num1 = 3
num2 = 5
product = 0 #lists global variables)
def something (something1, something2):
     global num1, num2 #typing a variable as global allows it to be operated within a function)
     num1 = 3
     num2 = 5
def some (num5, num3):
     global product #like a return function, calls product
     product = num5*num3

some (num1, num2)
something (num1, num2)
print (product) #recalls product out of global function
