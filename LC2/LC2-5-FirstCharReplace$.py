newarr = list()
string=input('Enter your String : ')
x=string[0]
j=-1
for i in string:
    j=j+1
    if i == x:
        newarr.append("$")
    else:
        newarr.append(string[j])
print(newarr)
