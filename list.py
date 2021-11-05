    # maakt een list
FloatList = [1.1, 2.2, 4.4, 8.8, 17.6, 35.2, 70.4, 140.8]
    # voegt iets achteraan toe
FloatList.append(420)
    # voegt iets toe waar je wilt
FloatList.insert(2, 69)
    # eigen attempt
for i in range(len(FloatList)):
    print(FloatList[i])
    # echte manier
for element in FloatList:
    print(element)
    # verwijderd getal voor maar safed als var
my_var = FloatList.pop(0)
my_var1 = FloatList.pop(0)

print(my_var + my_var1)

