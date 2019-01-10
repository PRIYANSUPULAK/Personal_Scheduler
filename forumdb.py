# Database for the app

import psycopg2
import bleach

# Name of database used
DBNAME = "forum"

# Returns all the posts from the database, most recent first


def get_posts():
    db = psycopg2.connect(database=DBNAME)
    # query to give all the posts from the table posts
    query = "select content, time from posts order by time desc;"
    c = db.cursor()
    c.execute(query)
    posts = c.fetchall()
    db.close()
    return posts

# Adding a post to the database with date and time


def add_post(content):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("insert into posts values (%s);", (bleach.clean(content),))
    # c.execute(query)
    db.commit()
    db.close()
