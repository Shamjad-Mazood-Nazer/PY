import csv
field_name = ['Sl. No', 'Brand', 'Phone Name']
car = [{'Sl. No': 1,'Brand':'Xiaomi','Phone Name':'Redmi 11 Max'},
    {'Sl. No': 2,'Brand':'Poco','Phone Name':'M2'},
    {'Sl. No': 3,'Brand':'Black Shark','Phone Name': 'Black Shark 4'},
    {'Sl. No': 4,'Brand':'ASUS', 'Phone Name':'ROG 5 ULTIMATE'},
    {'Sl. No': 5,'Brand':'Nokia', 'Phone Name':'ASHA 501'}]
with open('b.csv', 'w') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames = field_name)
    write.writeheader()
    write.writerows(car)
with open('b.csv', newline = '') as csvfile:
    d = csv.reader(csvfile, delimiter = '|')
    for r in d:
        print(','.join(r))
