mylist=[5,4,3,2,1]
newlist=[]
for i in range(len(mylist)):
    newlist.insert(i, mylist[-1])
    mylist.pop(-1)
print(newlist)
