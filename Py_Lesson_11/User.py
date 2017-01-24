import random
class User:
    def __init__(self, fName, lName, avat = ""):
        self.firstName = fName
        self.lastName = lName 
        self.avatar = avat
        self.userID = random.randint(0, 100000000)

    def setNames(self, fName, lName, avat):
        fName = setNames(firstName)
        lName = setNames(lastName)
        avat = setNames(avatar)
        userID = setNames(userID)
        
    def getfName(self):
        return self.firstName
    def getlName(self):
        return self.lastName
    def getavat(self):
        return self.avatar
    def getuID(self):
        return self.userID
    def __str__(self):
        return "Customer Info...\nFirst Name: " + self.firstName + "\nLast Name: " + self.lastName + "\nAvatar: " + self.avatar + "\nUser ID#: " + str(self.userID)
    
def main():
#   user1 = User(firstName, lastName)
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    user1 = User(firstName, lastName)
    ioj = input ("Would  you like to use a public avatar? (y or n): ")
    if ioj == "n":
        user1 = User(firstName, lastName)
    else:
        avatar = input("What would you like as your avatar name? ")
        user1 = User(firstName, lastName, avatar)
    def __str__(self):
        return "Customer Info...\nFirst Name: " + self.firstName + "\nLast Name: " + self.lastName + "\nAvatar: " + self.avatar + "\nUser ID#: " + str(self.userID)
    print(user1)
  
main()




