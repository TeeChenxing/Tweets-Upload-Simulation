import redis_twitterAPI as twAPI
import csv
import redis
import time
import random as rnd
from tweet_objects import Tweet
r = redis.Redis('localhost', 6379, decode_responses=True)


def postTweetTimer(filename):
    """
    :param filename: a .csv file
    :return: the time it takes the function to insert all the tweets information
    in the .csv file into redis
    """
    start = time.time()
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        i = 1
        for line in reader:
            tweet = Tweet(i, line[0], time.time(), line[1])
            twAPI.postTweet(tweet)

            i += 1

    end = time.time()
    elapsed_time = end - start
    return elapsed_time


def getTimelineTimer(x):
    """
    :return: the time it takes for the API to get x number of timelines from
    random users
    """
    start = time.time()

    for i in range(0, x):
        random_user_num = rnd.randint(1, 5)
        twAPI.getTimeline(random_user_num)

    end = time.time()
    elapsed_time = end - start

    return elapsed_time
