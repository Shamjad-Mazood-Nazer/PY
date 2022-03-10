STR = input('Enter your Word : ')
list1 = list()
for i in STR:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        list1.append(i)
print('Vowels in the list are : ', list1)
