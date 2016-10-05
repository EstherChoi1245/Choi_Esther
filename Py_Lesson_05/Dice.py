import random
playeroll = random.randint (1, 7)
computrol = random.randint (1, 7)


def rollDice (num1, num2):
    if playeroll > computrol:
        print ("You rolled a",playeroll)
        print ("The computer rolled a",computrol)
        print ("You're the winner!")
    
    
    if not playeroll > computrol:
        print ("You rolled a" ,playeroll)
        print ("The computer rolled a",computrol)
        print ("The computer won!")


print (rollDice(playeroll, computrol))
