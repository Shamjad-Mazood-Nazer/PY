import csv
with open('CSV1.csv') as file:
     data = csv.reader(file,delimiter = '\t')
     for row in data:
         print(row)
