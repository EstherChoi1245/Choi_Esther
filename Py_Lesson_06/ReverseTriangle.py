string = input ("Enter a word:")

def printf():
    for letter in range(len(string), 0, -1):
        print (string[0:letter])

printf()


