class Human:
    def __init__(self, hair="", eyes="", skin=""):  
        self.h = hair
        self.e = eyes
        self.s = skin
        
    def setHES(self, hair, eyes, skin):  
        hair = setHES(h)
        eyes = setHES(e)
        skin = setHES(s)


    def getHair(self):
        return self.h
    def getEyes(self):
        return self.e
    def getSkin(self):
        return self.s
    
def main():
    hair = input("Enter in a hair color:")
    eyes = input("Enter in an eye color:")
    skin = input("Enter in a skin color:")
    something = Human(hair, eyes, skin);
    print ("My info....")
    print ("Hair:", something.getHair())
    print ("Eyes:", something.getEyes())
    print ("Skin:", something.getSkin())


    newinfo = Human("blonde", "blue", "white");
    print ("Friend's info....")
    print ("Hair:", newinfo.getHair())
    print ("Eyes:", newinfo.getEyes())
    print ("Skin:", newinfo.getSkin())

main()


