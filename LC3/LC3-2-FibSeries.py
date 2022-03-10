n = int(input("Enter Your Limit : "))
a = 0
b = 1
print(a)
print(b)
for i in range(1, n):
    x = a+b
    a = b
    b = x
    print(x)
