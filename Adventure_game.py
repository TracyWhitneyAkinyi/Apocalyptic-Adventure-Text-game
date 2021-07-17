import time

answer_1 = ["A", "a"]
answer_2 = ["B", "b"]
answer_3 = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Objects that may be needed
gun = 0
keys = 0
backpack = 0
torch = 0

required = "\n You can only use A, B or C \n"


# The story begins as follows


def introduction():
    print("\nYou are in a post apocalyptic world. Aliens have taken over. Everything is in chaos.\n"
          "\nIt is a matter of survival for the fittest.Aliens are tracking down the human population,\n"
          "\nand killing them on sight. You and the remaining of the human population are in hiding.\n"
          "\nThere is a hidden location for food and supplies for the humans.\n"
          "\nBut you have to be witty since most of the humans have been killed on their way for bthe supplies.\n"
          "\nYou live with a group of friends and it is your turn to go get supplies.\n"
          "\nNone of your friends know the location. You leave the area of hiding and...\n")
    time.sleep(1)
    print("""
             A.Use the sewer manhole.
             B.Get out of your location and use the footpath
             C.Take the nearby motorcycle   """)
    choice = input(">")
    if choice in answer_1:
        option_sewer()

    elif choice in answer_2:
        option_footpath()

    elif choice in answer_3:
        print("\nDude!Your motorcycle alerted the aliens nearby.You are spotted and killed\n"
              "\nYou died!")
    else:
        print(required)
        introduction()


def option_sewer():
    print("\nAfter walking a distance ,you come across writing on the wall.\n"
          "\n Dragons1249 . On the left you come across a gun,a backpack,keys and a torch.\n"
          "\nDo you pick the items. Y/N? ")
    choice = input(">")
    if choice in yes:
        gun = 1  # adds gun
    else:
        gun = 0
    if choice in yes:
        backpack = 1  # adds backpack
    else:
        backpack = 0
    if choice in yes:
        keys = 1  # adds keys
    else:
        keys = 0
    if choice in yes:
        torch = 1  # adds torch
    else:
        torch = 0
    print("\nYou climb out of the sewer manhole to the desolate town and now you have to be extra cautious.\n"
          "\nOh!Oh! You just bumped into an alien. You need to think fast. What do you do?\n")
    time.sleep(1)
    print("""
            A.Shoot the alien using the gun.
            B.Run.
            C.Attack with your bare hands. """)
    choice = input(">")
    if choice in answer_1:
        option_gun()
    elif choice in answer_2:
        option_run()
    elif choice in answer_3:
        print("\nAre you Superman? Anyway,the alien tore you to shreds.Au revior!\n")
    else:
        print(required)
        option_sewer()


def option_footpath():
    print("\nYou have to be careful,you could be spotted. Oh! Oh! You just bumped into an alien.\n"
          "You need to think fast.What do you do?\n")
    time.sleep(1)
    print("""
            A.Shoot the alien using the gun.
            B.Run.
            C.Attack with your bare hands. """)
    choice = input(">")
    if choice in answer_1:
        print("\nYou don't have a gun. Anyway, the alien just killed you.Ciao!\n")
    elif choice in answer_2:
        option_run()
    elif choice in answer_3:
        print("\nAre you Superman? Anyway,the alien tore you to shreds.Au revior!\n")
    else:
        print(required)
        option_footpath()


def option_gun():
    print("Good.It's dead.The gunshot has alerted the other aliens in the surrounding.\n"
          "\n However there is a room written Safehouse. Do you have key?Y/N\n")
    choice = input(">")
    if choice in yes:
        option_safe()
    else:
        print("\n You are done for!You need key to open Safehouse. I guess that's it.\n"
              "\n The aliens caught up with youYou died!\n")
        option_gun()


def option_run():
    print("Wow! You eluded the alien. You however need to hide in a room written Safehouse.\n"
          "\nDo you have key? Y/N\n")
    choice = input(">")
    if keys > 0:
        option_safe()
    else:
        print("\nSorry dude.You can't keep running forever.You need to hide in the Safehouse.\n"
              "\nThe aliens have caught up with you.\n"
              "\nYou died")
        option_run()


def option_safe():
    print("You managed to enter the Safehouse and wait of the patrolling aliens.\n"
          "You notice there is a torch.Do you pick it?")
    choice = input(">")

    if torch > 0:
        print("\nTh exit of the Safehouse leads to a dark cave.\n"
              "\nYou turn on your torch light.And notice there is a steep valley.\n"
              "\nLuckily,you can make it to the other side in a single jump\n")
        option_jump()
    else:
        print("\nOkay...Let's move on.The exit of the Safehouse leads to a dark cave.\n"
              "\nYou can't see what's in front of you.What do you do?")
        time.sleep(1)
        print("""
                A. Keep walking ahead.
                B. Decide to crawl .
                C.Take a huge jump.
                """)
        choice = input(">")
        if choice in answer_1:
            print("\nOops! There was a steep valley.You could have made it in a single jump.\n"
                  "\nYou died\n")
        elif choice in answer_2:
            print("\nOops! There was a steep valley.You could have made it in a single jump.\n"
                  "\nYou died\n")
        elif choice in answer_3:
            option_jump()
            print("\nWoow!You lucky goose. You survived the steep valley.\n")
        else:
            print(required)
            option_safe()


def option_jump():
    print("\nYeiiy! You are 2 metres to the supplies station. There is a large gate.\n"
          "\nHowever to the right there is a 4-password system.It shows _42_.\n"
          "\nIf you used the sewer,you are in luck.However,you have one shot.\n"
          "\nIf you enter the wrong password.You will be vaporized.\n"
          "\nThe vaporizing machine was placed for extra security\n"
          "\nTo jog your memory, you have three choices.What is the right choice?")
    time.sleep(1)
    print("""
            A. 3,6
            B. 1,9
            C. 5,7
            """)
    choice = input(">")
    if choice in answer_1:
        print("\nWrong password.You were vaporized to death.\n")
    elif choice in answer_2:
        option_entry()
    elif choice in answer_3:
        print("\nWrong password.You were vaporized to death\n")
    else:
        print(required)
        option_jump()


def option_entry():
    print("You are finally in. The supplies station can finally give you the supplies for the month.\n"
          "\nAnd guess what? You get to be teleported back to your initial location.\n"
          "\nHowever you need a backpack,to secure the supplies.The teleportation machine has one fault.\n"
          "\nIt interferes anything that isn't of human DNA.\n"
          "\nThis means that will turn you into the inanimate object you are carrying.\n"
          "\nThe backpack prevents that from happening.Exit out of the station is prohibited\n")
    time.sleep(1)
    if backpack > 1:
        print("\nMission Complete.You have won The game!Game over.")
    else:
        print("\nSorry dude, you lost.Game over.")


introduction()
