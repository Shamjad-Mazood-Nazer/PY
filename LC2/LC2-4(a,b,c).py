list1 = []
list2 = []
m = int(input("enter the limit of List1 : "))
n = int(input("enter the limit of List2 : "))
for i in range(0, m):
    a = int(input('Enter the values of list1 : '))
    list1.append(a)
for j in range(0, n):
    b = int(input('Enter the values of list2 : '))
    list2.append(b)

#check whether the list are of same length
if len(list1) == len(list2):
    print("The length of List1 and Liat2 are same length.")
else:
    print("The length of List1 and List2 are not same length.")

#check whether the sum are equal
sum1 = sum(list1)
sum2 = sum(list2)
if sum1 == sum2:
    print('Sum equal')
else:
    print('Sum Different')

#check whether same elements occurred in both list
for i in list1:
    if i in list2:
        print(i, ' is in both list')