colorlist1 = ["red","blue","green"]
colorlist2 = ["red","blue","pink"]
print('Color List 1 : ', colorlist1)
print('Color List 2 : ', colorlist2)
c1 = set(colorlist1)
c2 = set(colorlist2)
x = c1.difference(c2)
colorl = list(x)
print('New Color List : ', colorl)
