def thing (number):
    output = ("{:8.4f}".format(number))
    return output

principal = float(input("How much is in the bank account initially?"))
rate = float(input("What is the rate of interest?"))
compound = float(input("How many times is the interest compounded in a year?"))
life = float(input("What is the life of the loan in years?"))

rn = rate / compound
cl = compound * life

print ("You will have" ,(thing(((rn+1)**(cl))*principal)),"in",life,"years.")
