print("You wake up in the morning and find your self standing in the dessert. what do you do?")
print("A. Go back to sleep")
print("B. Start walking in a random direction")
choice = input()
if choice == 'A':
    print("You go back to sleep to never wake up")
elif choice == 'B':
    print("You start walking in a random direction and find a gas station. what do you do?")
    print("A. Continue walking")
    print("B. Go into the gas station")
    choice1 = input()
    if choice1 == 'A':
        print("After hours of walking you fall down of dehydration")
    elif choice1 == 'B':
        print("You walk into the gas station and you see  man behind the counter. What do you do?")
        print("A. take some food and water and run away")
        print("B. Go and talk to the man")
        choice2 = input()
        if choice2 == 'A':
            print("the man chases after you with a shotgun and kills you")
        elif choice2 == 'B':
            print("The man ask what you want to know")
            print("A. You ask him where the nearest town is")
            print("B. you tell him this is a robbery")
            choice3 = input()
            if choice3 == 'A':
                print("The man tells you it's a half hour walk to the east. What do you do?")
                print("A. Ask the man why there is a gas station in the middle of nowhere")
                print("B. Start walking in the direction that you where told")
                choice4 = input()
                if choice4 == 'A':
                    print("The man tells you that there is a methlab beneath the gas station and they just found a new employe")
                    print("you are forced to work in the methlab for 2 years before being rescued by the police")
                elif choice4 == 'B':
                    print("After a half hour walk you find the town and get a drive home you safely made it")
                else:
                    print("please choice A or B")
            elif choice3 == 'B':
                print("The man grabs a shotgun and shoots you")
            else:
                print("please chooce A or B")
        else:
            print("please chooce A or B")
    else:
        print("please chooce A or B")
else:
    print("please chooce A or B")
