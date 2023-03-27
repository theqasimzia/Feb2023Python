import csv

filename = "potibo.csv"

with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
        print(row)