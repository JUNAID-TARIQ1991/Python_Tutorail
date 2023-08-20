import csv
with open("Data.csv") as file:
    reader = csv.DictReader(file, delimiter=",")
    # print(list(reader))
    for row in reader:
        print(row)
