sentence = input("Write a sentence")

top = 0
def replace(sentence1, num):
    global sentence
    if (sentence.count(" ")<=0):
        return sentence
    else:
        sentence = sentence[0:sentence.index(" ")] + "_" + sentence[sentence.index(" ")+1: len(sentence)]
        replace (sentence, (top + 1))
        return sentence
        

replace (sentence, top)
print (sentence)
    
