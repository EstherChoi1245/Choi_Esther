def thing (number):
    output = ("{:0.2f}".format(number))
    return output

principal = float(input("How much is in the bank account initially?"))
rate = float(input("What is the rate of interest?"))
compound = float(input("How many times is the interest compounded in a year?"))
life = float(input("What is the life of the loan in years?"))

balance= ((principal*(1+(rate/compound))**(compound*life))/(life*12))

print ("You will have $",thing(balance),"in",life,"years.")
