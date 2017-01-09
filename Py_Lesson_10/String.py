go = input("Please enter 16 strings:")

def split(go):
    global smth
    smth = []
    smth.append(go)
    
split(go)

wordsList= [""]
spot = 0
for i in range(0, 4):
    output = [""]
    wordsList.append([""])
    for j in  range(0, 4):
        wordsList.append(split(spot))
        output.append(wordsList[i][j]) 
        spot+= 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    print(output)
    




