Using `sqlite3`, a command-line program that lets us use another language, SQL to achieve the same result.

Create a new database called favorites.db and import our CSV file into a table called “favorites”:

    ~/ $ sqlite3 favorites.db
    SQLite version 3.22.0 2018-01-22 18:45:57
    Enter ".help" for usage hints.
    sqlite> .mode csv
    sqlite> .import "CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv" favorites