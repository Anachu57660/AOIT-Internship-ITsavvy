import csv


with open('Bundle_Spreadsheet.csv', 'r') as file:
    reader = csv.reader(file)
    line_count = 0
    list = []
    for row in reader:
        list.append(row)
        print(row)
    print()
    print(list)
    print()
    print(list[0][0])

