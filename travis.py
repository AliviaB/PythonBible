known_user=["Harry","Bob","Joerge","Alice","Tara","Peter"]

print(len(known_user))
del known_user[0]

while True:
    print("Hello! I am Travis!")
    name = input("What is your Name?")
    name=name.capitalize()
    if name in known_user :
        print("Hello",name)
        remove=input("Would you like to be removed (y/n):").lower()
        if remove=="y":
            known_user.remove(name)
    else:
        print("Hmm! I dont recognize you {} yet ".format(name))
        add=input("Would you like to be added to the system (y/n):").strip().lower()
        if add =="y":
            known_user.append(name)
