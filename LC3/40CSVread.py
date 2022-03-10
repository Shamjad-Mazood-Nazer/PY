import csv
with open("CSV1.csv", newline='') as csvfile:
    d = csv.DictReader(csvfile)
    print("Name Price Qty")
    print("--------------------")
    for i in d:
        print(i['Name'], i['Price'], i['Qty'])
