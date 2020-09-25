Using `sqlite3`, a command-line program that lets us use another language, SQL to achieve the same result.

Create a new database called favorites.db and import our CSV file into a table called “favorites”:

    ~/ $ sqlite3 favorites.db
    SQLite version 3.22.0 2018-01-22 18:45:57
    Enter ".help" for usage hints.
    sqlite> .mode csv
    sqlite> .import "CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv" favorites

We see a favorites.db in our IDE after we run this, and now we can use SQL to interact with our data. The following command grabs all the TV show titles. It basically selects a column from a table in your DB:

    sqlite> SELECT title FROM favorites;

This lets us sort the results (same results as above query) in alphabetical order:

    sqlite> SELECT title FROM favorites ORDER BY title;

Using GROUP BY will consolidate the entries in a column thus removing duplicates:

    sqlite> SELECT title FROM favorites GROUP BY title  ORDER BY title;

This gives us a count of the number of times each title appears. Note that COUNT(title) on its own returns just one integer:

    sqlite> SELECT title, COUNT(title) FROM favorites GROUP BY title;

Notice that so far to date we have achieved what we did with python code but quicker and without having to worry about coding.

SQL is a language that lets us work with a relational database, an application lets us store data and work with them more quickly than with a CSV.

With .schema, we can see how the format for the table for our data is created. It shows us the data structure: 

    sqlite> .schema
    CREATE TABLE favorites(
        "Timestamp" TEXT,
        "title" TEXT,
        "genres" TEXT
    );

We can even set the count of each title to a new variable, n, and order our results by that, in descending order. Here's how we see the top 10 results:

    sqlite> SELECT title, COUNT(title) AS n FROM favorites GROUP BY title ORDER BY n DESC LIMIT 10;

We can do some data cleansing using:

    sqlite> UPDATE favorites SET title = "The Office" WHERE title LIKE "%office"

That will set all the rows with the title containing “office” to be “The Office” so we can make them consistent.
