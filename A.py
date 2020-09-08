import csv


with open('AOIT_Internship_Excel.csv', 'r') as file:
    reader = csv.reader(file)
    line_count = 0
    for row in reader:
        print(row)