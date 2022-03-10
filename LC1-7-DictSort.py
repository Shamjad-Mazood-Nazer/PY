def dictionairy():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    print("ASCENDING ORDER :-\n")
    print("Values are")
    for i in sorted(key_value.values()):
        print(i, end=" ")
    print("\nDESCENDING ORDER :-\n")
    print("Values are")
    for i in sorted(key_value.values(), reverse=True):
        print(i, end=" ")


dictionairy()
