def stringfunctie(s):   
    s = s[0:len(s)-1]
    if len(s) != 0:
        print(s)
        stringfunctie(s)
    elif len(s) == 0:
        print(" ")
        return

me = "Hallo ik ben een string en ik wordt opgegeten"
    
food = "halllllllooooooooooooooooooooooooooo"
stringfunctie(me)
stringfunctie(food)
