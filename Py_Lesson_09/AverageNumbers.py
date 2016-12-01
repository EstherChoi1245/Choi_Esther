import random
numbers= []

for i in range(0, 10):
    numbers.append(str(random.randint(1, 100)))
    
print ("Numbers....")
output = ""

for string in numbers:
    output+= " " + string + output

print (output + "\n")

def average(num1):
    global nums, num, average1
    average1 = 0
    nums= ""
    for num in nums:
        average1 = num+ numbers
    return int(average1%10(numbers.count))

print("The average of the above numbers is...." + average(numbers))

