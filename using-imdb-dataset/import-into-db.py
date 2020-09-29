import csv
import cs50

# create an empty file ready to receive data and then close it
open("shows2.db", "w").close()

# open for SQLite
# for this to work a file called shows2.db needs to exist first, hence the above step
db = cs50.SQL("sqlite:///shows2.db")

# create table called shows in database file called shows2.db
db.execute("CREATE TABLE shows (tconst TEXT, primaryTitle TEXT, startYear NUMERIC, genres TEXT)")
db.execute("INSERT INTO shows (tconst, primaryTitle, startYear, genres) VALUES (\"monkey\", \"mokey\", 12, \"sakaisdf\");")

# # open title.basics.tsv
# with open("title.basics.tsv", "r") as titles:

#     # create DictReader
#     reader = csv.DictReader(titles, delimiter="\t")

#     for row in reader:

