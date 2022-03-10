mylist=list()
N=int(input('Enter the limit : '))
for i in range(N):
    a=int(input("Enter the value : "))
    if a > 99:
        mylist.append('OVER')
    else:
        mylist.append(a)
print("List is : ", mylist)
