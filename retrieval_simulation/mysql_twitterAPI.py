import pandas as pd


def post_tweet(api, cursor, user_id, tweet_txt):
    """
    :param api: name of api the cursor will execute from
    :param cursor: name of cursor
    :param user_id: user id number, must be integer
    :param tweet_txt: a string containing one's desired tweet
    :return: insert into the database one's desired tweet
    """
    insert_stmt = ("INSERT INTO tweets (user_id, tweet_text) VALUES (%s, %s)")
    cursor.execute(insert_stmt, (user_id, tweet_txt))
    api.commit()


def get_timeline(cursor, user_id, limit):
    """
    :param cursor: name of cursor
    :param user_id: user id number, must be integer
    :param limit: top # of rows from the select statement
    :return: a dataframe for the user_id's timeline and its relevant information
    """

    timeline_tweets_stmt = ("select follows.USER_ID, follows.FOLLOWS_ID, tweets.tweet_ts, tweets.tweet_text "
                            "from follows "
                            "join tweets on follows.FOLLOWS_ID = tweets.user_id "
                            "where follows.USER_ID = %s "
                            "order by tweets.tweet_ts DESC "
                            "limit %s; ")

    cursor.execute(timeline_tweets_stmt, (user_id, limit))
    tweets_ls = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    df = pd.DataFrame(tweets_ls, columns=field_names)

    return df


def get_followers(cursor, user_id):
    """
    :param cursor: name of cursor
    :param user_id: user id number, must be integer
    :return: a dataframe of who is following that user_id
    """

    find_followers_stmt = ("select USER_ID "
                            "from follows "
                            "where FOLLOWS_ID = %s ")

    cursor.execute(find_followers_stmt, (user_id,))
    followers_ls = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    df = pd.DataFrame(followers_ls, columns=field_names)

    return df


def get_followees(cursor, user_id):
    """
    :param cursor: name of cursor
    :param user_id: user id number, must be integer
    :return: a dataframe of whom the user_id is following
    """

    find_followees_stmt = ("select FOLLOWS_ID "
                            "from follows "
                            "where USER_ID = %s ")

    cursor.execute(find_followees_stmt, (user_id,))
    followers_ls = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    df = pd.DataFrame(followers_ls, columns=field_names)

    return df


def get_tweets(cursor, user_id):
    """
    :param cursor: name of cursor
    :param user_id: user id number, must be integer
    :return: a dataframe of the tweets posted by that user_id
    """

    find_tweet_stmt = ("select tweet_text "
                            "from tweets "
                            "where USER_ID = %s ")

    cursor.execute(find_tweet_stmt, (user_id,))
    followers_ls = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    df = pd.DataFrame(followers_ls, columns=field_names)

    return df
