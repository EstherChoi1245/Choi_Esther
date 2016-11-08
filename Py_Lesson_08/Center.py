one = input("Enter your first word:")
two = input("Enter your second word:")
three = input("Enter your third word:")
top = 0


def makeCenter (word):
    if len(word)>=20:
        return (word)
    else:
        word = " " + word + " "
        return makeCenter(word)


print (makeCenter(one))
print (makeCenter(two))
print (makeCenter(three))

