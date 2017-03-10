user1 = int(input("Please enter your starting number:"))
user2 = int(input("Please enter your sequence size:"))

seq= []
output = ""

for i in range(0, user2):
    if i==0 or i==1:
        seq.append(user1)
    else:
        seq.append(seq[i-1]+seq[i-2])
    output+= str(seq[i]) + " " 

print (output)

