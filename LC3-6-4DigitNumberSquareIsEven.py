Low_Limit = int(input('Enter the Low_Limit : '))
High_Limit = int(input('Enter the High_Limit : '))
print('The Digits are :')
for i in range(Low_Limit, High_Limit):
    if i**0.5 == int(i**0.5):
        print(i)
