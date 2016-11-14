word = input("Enter a word:")
stop = len(word)
start = 0
def tree (word, start, stop):
    if start <= stop:
        print ("{:>6}".format(word[0:start]))
        start+=1
        tree (word, start, stop)        
    else:
        return 0 
        
tree (word, start, stop)











