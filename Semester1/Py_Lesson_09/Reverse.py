
words = ["something.", "over", "jumped", "dog", "The"]
print ("In order....")
lst = ""

for word in words:
    lst += word + " "
print(lst + "\n")

print ("Reversed....")  

def rev (words):
    output = ""
    for i in range(len(words)-1, -1, -1):
        output += words[i] + " "
    print(output)
        
rev(words)





