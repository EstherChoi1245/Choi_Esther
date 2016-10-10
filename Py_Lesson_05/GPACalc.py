science = input("What letter grade do you have in your science class right now?")
math = input("What letter grade do you have in your math class right now?")
english = input("What letter grade do you have in your english class right now?")
history = input("What letter grade do you have in your history class right now?")
PE = input("What letter grade do you have in your PE class right now?")
language = input("What letter grade do you have in your langauge class right now?")
art = input("What letter grade do you have in your art class right now?")
A = 0
B = 0
C = 0
D = 0
F = 0

def calcPoints(num1):
    global A, B, C, D, F
    if num1 == A:
        return 4.0
    elif num1 == B:
        return 3.0
    elif num1 == C:
        return 2.0
    elif num1 == D:
        return 1.0
    else:
        return 0.0

print("Your GPA is", (calcPoints (science) + calcPoints (math) + calcPoints (english) + calcPoints (history) + calcPoints (PE) + calcPoints (language) + calcPoints (art))/7)





   





    
