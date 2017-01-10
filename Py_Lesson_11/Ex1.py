class MilesPerHour:
    def __init__(self, distance="", hours="", minutes=""):
        self.distance =  distance
        self.hours = hours
        self.minutes = minutes
        mph = 0
    def setValues(self, distance, hours, minutes):
        distance = setValues(distance)
        hours = setValues(hours)
        minutes = setValues(minutes)
        mph = 0
    def GetDist(self):
        return self.distance
    def getHours(self):
        return self.hours
    def getMins(self):
        return self.minutes
    def getMPH(self):
        mph = distance/(hours + minutes/60.0)
        return mph
def main():
    global distance, hours, minutes

    distance = int(input("Please enter a distance:"))
    hours = int(input("Please enter a hours:"))
    minutes = int(input("Please enter a minutes:"))
    
    object1 = MilesPerHour(distance, hours, minutes)

    print ("Miles: ", object1.GetDist(), "\n")
    print ("Hours: ", object1.getHours(), "\n")
    print ("Minutes: ", object1.getMins(), "\n")
    
    print ("MPH: ", object1.getMPH(), "\n")

main()

    
    
    
