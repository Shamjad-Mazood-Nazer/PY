start = 2021
end = int(input('Enter End year : '))
print("Leap year from {} to {} are :\n".format(start, end))
for year in range(start, end):
    if 0 == year % 4 and 0 != year % 100 or 0 == year % 400:
        print(year)
