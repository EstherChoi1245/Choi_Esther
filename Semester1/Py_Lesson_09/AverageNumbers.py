
import random
numbers= []

for i in range(0, 10):
    numbers.append(random.randint(1, 100))
    
print ("Numbers....")
output = ""

for string in numbers:
    output= " " + str(string) + output

print (output + "\n")

def average(numbers):
    average1= 0
    nums=numbers
    for num in nums:
        average1+= num
    return average1/(len(nums))

print("The average of the above numbers is....", average(numbers))

