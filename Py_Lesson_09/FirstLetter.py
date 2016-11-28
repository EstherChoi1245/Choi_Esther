words = ["But", "ice cream", "tangents", "can't", "help"]
def first (words):
    something= words.split()
    print (something)
    output = " "
    j=0
    for i in words:
        output+= str(i)
        if j < len(words)-1:
            output+= " "
        j+=1
    print(output)

first(words)




