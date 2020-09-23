import csv

with open("response-data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)