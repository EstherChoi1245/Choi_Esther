countby= int(input("Enter the common difference:"))
end = int(input("Enter the end number:"))
output="0"

for i in range (countby, end+1, countby):
    output= output+" "+str(i)+" "
print(output)



    
