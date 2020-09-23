import csv

counts = {}

with open("response-data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"]

        if title in counts:
            counts[title] += 1
        else:
            counts[title] = 1 

for title, count in counts.items():
    print(title, count, sep=" | ")
