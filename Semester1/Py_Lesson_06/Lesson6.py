#for defines how many times
#i is a variable that controls the iteration
#top of the range is exclusive
#output = ""
#for i in range(2,-10, -2):
 #   output = output+ str(i)+ " "
#print (output)
    
need = int(input("Please enter the number of cookies you need: "))
batchSize = 25
batch = 1

for cookies in range(need, -1, -batchSize):
    print ("Cookies Needed: ", cookies)
    print ("Batch number: ", batch)
    batch = batch + 1

print ("Order up!")



    
