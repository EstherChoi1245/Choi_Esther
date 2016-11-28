#words = ["something", "over", "jumped", "dog", "The"]
#print ("In order....")

#print (words)

#print ("Reversed.....")

#myList = []
#output = " "
#j = 0

#for i in words:
 #   output += str(i)
  #  if  j < len(words):
   #     output+= i+1
        
#print (words)


    

#li= " "

#def reverse ():
 #   for r in range (len(words), 0, -1):
  #      li = li + str(r)

    
#reverse()

#print ([myList[5:0]])

myList = ["something.", "over", "jumped", "dog", "The"]
words = []

def rev (myList):
    output = " "
    for i in range(len(words)-1, -1, -1):
        output += myList[i]
        print (output)
            
rev(myList)

print ("In order....")

j = 0
output = " "
for i in myList:
    output += str(i)
    if j < len(myList): 
        output += " "
    j+=1
    print (output)

print ("Reversed....")

something = " "
for i in range (len(words)-1, -1, -1):
    something += rev(myList[i])

print (something) 
