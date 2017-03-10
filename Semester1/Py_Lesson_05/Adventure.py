
print ("Hey, you\'re going to the Fields to pick rare herbs for Madame Butterfly, right? I'll be coming with you.")

choice = input("There's a large cliff with a dangerous road winding through it but it's a shortcut to the Fields. There's a small path leading through the forest on the right but Butterfly needs those herbs fast. Do you want to take the long way or the short way? \n I want to take the:")
choice1 = "long way"
choice2 = input ("After a couple days of traveling, you arrive at the Fields, full of poisonous plants and exotic bugs. Madame Butterfly told you to pick \'a spiky, green plant with purple buds\', but there are two different plants that match that description. You only have enough room to carry one of the plants. Will you take plant a or plant b? \n I'm going to take plant:")
a = "a"
choice3 = input("You are about to pick the plant, but suddenly remember something Butterfly told you: it's very fragile but covered in extremely dangerous poison. You don't want to wear your heavy gloves because you might damage the plant, but you might get cut and poisoned. Will you wear the gloves? Put yes or no:")
b = "Yes"
c= "No"
if choice == choice1:
    if choice2 == a:
        if choice3 ==b:
            print ("You picked the right plant very carefully with your trusty gloves and carried it successfully to Madame Butterfly! Congrats!")
        else:
            print ("You picked the right plant! Unfortunately, because you didn't wear the gloves, your hands were cut to pieces and you died of poison and blood loss!")
    else:
        if choice3 == c:
            print ("You wore the gloves but picked the wrong plant and Butterfly died! Awww!")
        else:
            print ("After picking the wrong plant without gloves, your hands were shredded like grated cheese and you died of blood loss.")
else:
    if choice==a:
        if choice2==b:
            print ("You picked the right plant very carefully with your trusty gloves and carried it successfully to Madame Butterfly! Congrats!")
        else:
            print ("You picked the right plant! Unfortunately, because you didn't wear the gloves, your hands were cut to pieces and you died of poison and blood loss!")
    else:
        if choice3==c:
            print ("You wore the gloves but picked the wrong plant and Butterfly died! Awww!")    
        else:
            print ("After picking the wrong plant without gloves, your hands were shredded like grated cheese and you died of blood loss.")    






            
