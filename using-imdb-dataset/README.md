## IMDb data sourced using

    $ wget https://datasets.imdbws.com/title.basics.tsv.gz
    $ gunzip title.basics.tsv.gz

However the main zip file is 500MB+ (over 7M lines of data!) and surpasses GitHub's 100MB file limit. So will not commit that.

However we ran an import script that reduced that down significantly to 100K and 10K respectively (see `shows0.csv` and `shows1.csv`).

