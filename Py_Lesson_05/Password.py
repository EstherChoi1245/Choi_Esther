username = "TheLord"
password = "something"
def passCheck():
    username = input("Please enter your username:")
    password = input("Please enter your password:")
    if username=="TheLord" and password == "something":
        print ("You are granted access!")
    elif username=="TheLord": 
        print ("Your password is incorrect!")
    elif password=="something":
        print ("Your username is incorrect!")
    else:
        print ("Your username and password are incorrect!")

passCheck()
