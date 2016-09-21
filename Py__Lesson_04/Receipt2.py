
def printf (thing, something):
	print ("* {:>13}\t{:>10.7} *".format(thing, something))

thing2 = input("Enter your first name: ")
something2 = input("Enter your last name:")

thing1 = input("Enter the school site: ")
something1 = input("Enter the school year: ")

thing3 = input("Enter your title: ")
something3 = input("What is your subject? ")

print ("***************************")
printf (thing1, something1)
printf (thing2, something2)
printf (thing3, something3)
print ("***************************")

