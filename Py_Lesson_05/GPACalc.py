science = input("What letter grade do you have in your science class right now?")
math = input("What letter grade do you have in your math class right now?")
english = input("What letter grade do you have in your english class right now?")
history = input("What letter grade do you have in your history class right now?")
PE = input("What letter grade do you have in your PE class right now?")
language = input("What letter grade do you have in your langauge class right now?")
art = input("What letter grade do you have in your art class right now?")
A = 1
B = 1
C = 1
D = 1
F = 1
points = 0

    #global A, B, C, D, F
def calcP (letter):
    #global science, math, english, history, PE, language, art
    if letter == "A":
        return 4 
    elif letter == "B":
        return 3
    elif letter == "C":
        return 2
    elif letter == "D":
        return 1
    elif letter =="F":
        return 0

print ("Your GPA is :{:2.2}".format((calcP(art)+calcP(science)+calcP(math)+calcP(history)+calcP(language)+calcP(english)+calcP(PE))/7))



    
