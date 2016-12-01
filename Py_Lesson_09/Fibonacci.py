user1 = int(input("Please enter your starting number:"))
user2 = int(input("Please enter your sequence size:"))

seq= []

for i in range(0, user2):
    if i==0==1:
        seq= user1
    else:
        seq= (seq[user2] + seq[user2-1])

