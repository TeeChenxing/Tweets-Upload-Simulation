import csv
import random as rnd
import time


def post_tweet_timer(filename, cursor, api):
    """
    :param filename: a .csv where we will take data from and insert into a database
    :param cursor: name of cursor
    :param api: name of API the cursor will execute from
    :return: the time in takes to insert all the data from .csv file into a database
    """

    insert_stmt = ("INSERT INTO tweets (user_id, tweet_text) VALUES (%s, %s)")

    start = time.time()
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(f)
        for line in reader:
            cursor.execute(insert_stmt, (int(line[0]), line[1]))
            api.commit()

    end = time.time()
    elapsed_time = end - start

    return elapsed_time


def find_timeline_timer(cursor, limit):
    """
    :param cursor: name of cursor
    :param limit: top # of rows from the select statement
    :return: time it takes to run 100 select statements
    """

    select_statement = ("select follows.USER_ID, follows.FOLLOWS_ID, tweets.tweet_ts, tweets.tweet_text "
                        "from follows "
                        "join tweets on follows.FOLLOWS_ID = tweets.user_id "
                        "where follows.USER_ID = %s "
                        "order by tweets.tweet_ts DESC "
                        "limit %s; ")


    start = time.time()
    for i in range(1, 101):
        random_user_num = rnd.randint(1, 10000)
        cursor.execute(select_statement, (random_user_num, limit))

    end = time.time()
    elapsed_time = end - start

    return elapsed_time



