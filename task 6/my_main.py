import my_game

# St. Pylyp Orlyk
orlyk = my_game.Street('St. Pylyp Orlyk')
orlyk.set_description("Home")

olesia = my_game.Zbuj("Olesia", "gold")
olesia.set_description("The thief of all that shines\nShe stole gold from \
the jewelry store\nWould you catch her and pick up the stolen?\n\
(If yes, print 'catch', else print 'continue')")
orlyk.set_bad_character(olesia)

mariia = my_game.KindLaydak("Mariia")
mariia.set_description("Poor little girl asks you for help\n\
Would you give her some gold?\n(If yes, print 'help', else print 'continue')")
mariia.set_hint("Thing that gives person a lot of new knowlege could help you to win Ivan")
orlyk.set_kind_character(mariia)


# St. Lesia Ukrainka
ukrainka = my_game.Street('St. Lesia Ukrainka')
ukrainka.set_description("First location")

roman = my_game.Kavaler("Roman", "097-777-77-77")
roman.set_description("Brave gentleman could help you to win 1 killer\nYou can call him whenever \
you want\nWould you take his phone number?\n(If yes, print 'take', else print 'continue')")
ukrainka.set_kind_character(roman)

petro = my_game.Zbuj("Petro", "book")
petro.set_description("Brutal man that loves to rob stores\n\
This time he stole a precious book\nWould you catch him and pick up the stolen?\n\
(If yes, print 'catch', else print 'continue')")
ukrainka.set_bad_character(petro)


# St. Ivan Franko
franko = my_game.Street('St. Ivan Franko')
franko.set_description("Second location")

ivan = my_game.Killer("Ivan", "book")
ivan.set_description("He's been following you for a week\nHe didn't like your sneakers\n\
You must fight with him or you will lose")
franko.set_bad_character(ivan)


# St. Taras Shevchenko
shevchenko = my_game.Street('St. Taras Shevchenko')
shevchenko.set_description("Third location")


dmytro = my_game.Zbuj("Dmytro", "spider")
dmytro.set_description("A prankster thief who likes magic tricks with things disappearing\n\
This time he stole a spider from the zoo\n(If yes, print 'catch', else print 'continue')")
shevchenko.set_bad_character(dmytro)

pavlo = my_game.KindLaydak("Pavlo")
pavlo.set_description("Poor man who got lost\nHe asks you for help\n\
Would you give him some gold?\n(If yes, print 'help', else print 'continue')")
pavlo.set_hint("Something small with 8 legs could help you to win Bohdan")
shevchenko.set_kind_character(pavlo)


# Market Square8
square = my_game.Street('Market Square')
square.set_description("Fourth location")

bohdan = my_game.Killer("Bohdan", "spider")
bohdan.set_description("Stranger that lives in the town centre and frightens everybody\n\
You must fight with him or you will lose")
square.set_bad_character(bohdan)

# St. Sholem Aleichem
aleihem = my_game.Street('St. Sholem Aleichem')
aleihem.set_description("Fifth location")

oleg = my_game.Zbuj("Oleg", "knife")
oleg.set_description("Likes different weapons\nThis time he stole the knife\n\
Would you like to catch him?\n(If yes, print 'catch', else print 'continue')")
aleihem.set_bad_character(oleg)


# St. Stryjska
stryjska = my_game.Street('St. Stryjska')
stryjska.set_description("Sixth location")

nazar = my_game.Killer("Nazar", "gold")
nazar.set_description("Oddball who loves to make fun of people\n\
You must fight with him or you will lose")
stryjska.set_bad_character(nazar)


current_street = orlyk
route = [ukrainka, franko, shevchenko, square, aleihem, stryjska, orlyk]
backpack = []
start = f"""Hey!
Let's play 'blukachka' in Drohobych :)
Your first point is in St. Plypa Orlyka
To get back home(St. Plypa Orlyka) and win the game you have to pass: 
[{', '.join(i.name for i in route)}]"""
print(start)

call_roman = 1
dead = False

while dead is False:
    print('\n')
    current_street.get_details()

    inhabitant_bad = current_street.get_bad_character()

    if inhabitant_bad is not None:
        inhabitant_bad.describe()

    command1 = input('> ')
    if command1 == 'catch':
        if not isinstance(inhabitant_bad, my_game.Zbuj):
            print(f"Sorry, you cant't catch {inhabitant_bad.name}")
        else:
            print(f"Yeah! You caught {inhabitant_bad.name}")
            backpack.append(inhabitant_bad.stolen)
            print(f"Your backpack has been replenished {backpack}")
    elif command1 == 'fight':
        if not isinstance(inhabitant_bad, my_game.Killer):
            print(f"Sorry, you can't fight with {inhabitant_bad.name}")
        else:
            print("What would you like to fight with?")
            fight_with = input('> ')
            if fight_with in backpack:
                if inhabitant_bad.fight(fight_with):
                    print(f"Yeah! You won the killer {inhabitant_bad.name}")
                    backpack.remove(fight_with)
                    print(backpack)
                    inhabitant_bad = None
                else:
                    print("Unfortunately, you didn't guess")
                    print(f"{fight_with} didn't kill {inhabitant_bad.name}")
                    print("You lost...(")
                    break
            else:
                print(f"Unfortunately, you haven't {fight_with} in your backpack")
                print("You lost...(")
                break
    elif command1 == 'continue' and isinstance(inhabitant_bad, my_game.Zbuj):
        continue
    elif command1 != 'fight' and isinstance(inhabitant_bad, my_game.Killer):
        print("You lost...(")
        break
    else:
        print(f"I don't know how to {command1}\nTry again")


    inhabitant_kind = current_street.get_kind_character()

    if inhabitant_kind is not None:
        inhabitant_kind.describe()

        while True:
            command2 = input('> ')
            if command2 == 'help':
                if inhabitant_kind.need in backpack:
                    print("Thank you, kind man!")
                    print("For your kindness, here is a hint:")
                    print(inhabitant_kind.hint + '\n')
                else:
                    print("Unfortunately, you haven't enough gold to give")
                break
            elif command2 == 'take':
                backpack.append(inhabitant_kind.number)
                print("Call if you need my help")
                print("See you")
                break
            elif command2 == 'continue':
                break
            else:
                print(f"I don't know how to {command2}\nTry again")
        print('\n')

    print("Let's move to another street!")
    current_street = route.pop(0)
    print(current_street.name)
    if not route:
        print("Congratulations! You reach the St. Pylyp Orlyk")
        print("See you soon in Drohobych)")
        dead = True
