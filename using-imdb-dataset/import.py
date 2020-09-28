# the goal is to make the IMDB dataset more manageable. It currently contains some 7194770 lines as you can see by running $ wc -l title.basics.tsv

import csv

with open("title.basics.tsv", "r") as titles:
    reader = csv.DictReader(titles, delimiter="\t") # backslash t = tab character just like how backslash n = new line

    # if the file doesn't exist it is fine it will create one
    with open("shows1.csv", "w") as shows:
        writer = csv.writer(shows)

        # write the first header rows
        writer.writerow(["tconst", "primaryTitle", "startYear", "genres"])

        # iterating through original IMDB dataset title.basics.tsv
        for row in reader:
            # due to the idiosyncracies of IMDb data
            if row["startYear"] == "\\N":
                continue

            year = int(row["startYear"]) # since everything in a .tsv or .csv file is text
            if year >= 1970:
                continue

            if row["titleType"] == "tvSeries" and row["isAdult"] == "0":
                writer.writerow([row["tconst"], row["primaryTitle"], row["startYear"], row["genres"]])
