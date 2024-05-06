#!/bin/sh
    python3 load_tweets.py --db=postgresql://postgres:pass@localhost:2103/ --user_rows=50

# list all of the files that will be loaded into the database
# for the first part of this assignment, we will only load a small test zip file with ~10000 tweets
#but we will write are code so that we can easily load an arbitrary number of files
