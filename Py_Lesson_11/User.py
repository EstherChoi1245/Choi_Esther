class User:
    def __str__(self):
        return "Customer Info.... \nFirst Name: " + self.firstName + "\nLast Name: " + self.lastName + "\nAvatar: " + self.avatar + "\nUser ID#: " + str(self.UserID)
    
def main():
    user1 = User(firstName, lastName)
    ioj = input ("Would  you like to use a public avatar? (y or n)")
    if ioj == "n":
        user1
    if ioj == "y":
        aname = input("What would you like as your avatar name?")
        
        


main()    
