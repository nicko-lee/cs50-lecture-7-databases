import csv

with open("response-data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)