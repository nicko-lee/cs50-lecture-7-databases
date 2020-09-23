import csv

counts = {}

with open("response-data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"].lower() # standardize text to lowercase to prevent duplicates due to cases

        if title in counts:
            counts[title] += 1
        else:
            counts[title] = 1 

# to sort by value it is a bit different to sorting by key. Equivalent to just using a lambda or anonymous in-line func
# since you are only using this once no point defining it
# def f(item):
#     return item[1]

# passing in the function by name as a param to another function (not calling it)
for title, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    print(title, count, sep=" | ")
