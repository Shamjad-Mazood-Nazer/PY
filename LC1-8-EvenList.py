mylist = [1, 2, 3, 4, 5, 6]
print('List is : ', mylist)
print('New List is : ')
for i in mylist:
    if(i%2 != 0):
        newlist = [i]
        print(newlist)
