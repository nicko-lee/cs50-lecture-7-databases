import csv

# ask user for input
title = input("Title: ")

# open our filtered CSV (a significantly smaller subset than the original IMDb file)
# feel free to swap between shows0.csv or shows1.csv
with open("shows1.csv", "r") as file:  
    reader = csv.DictReader(file)

    # iterate over every row (over 10,000 rows) and check each row's title
    for row in reader:

        if title == row["primaryTitle"]:
            print(row["primaryTitle"], row["startYear"])