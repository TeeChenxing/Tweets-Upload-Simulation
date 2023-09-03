import csv
import redis
from tweet_objects import Tweet
r = redis.Redis('localhost', 6379, decode_responses=True)


def postTweet(tweet):
    """
    :param tweet: take in a tweet object that has the field
                  - unique tweetID
                  - userID who posted the text
                  - tweetTime (auto generated when tweet object is created)
                  - text of tweet
    :return: Function does not return a value but pushes the specified
    tweet into redis as a hash where it can be extracted with hgetall
    """

    r.hset(f"tweet{tweet.tweetID}", mapping={"tweet_id": tweet.tweetID,
                                             "user_id": tweet.userID,
                                             "tweet_ts": tweet.tweetTime,
                                             "tweet_text": tweet.tweetTXT})

    tweet = r.hgetall(f"tweet{tweet.tweetID}")

    # create a list of tweetIDs for the users that the specified userID who
    # posted the tweet follows.
    for usr in r.lrange(f"followees{tweet['user_id']}", 0, -1):
        r.lpush(f"timeline{usr}", tweet['tweet_id'])


def follows(user_num, dataset):
    """
    :param user_num: the userID parameter of the tweet object.
    :param dataset: can either be "follows.csv" or "follows_sample.csv"
    for testing purposes
    :return: a list of userID that the user_num follows
    """

    with open(dataset, "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)

        for line in reader:
            # follower of line[0] follows the userID of <line[1]>
            r.lpush(f"follows{line[0]}", line[1])

    ls_of_follows = r.lrange(f'follows{user_num}', 0, -1)
    return ls_of_follows


def followees(user_num, dataset):
    """
    :param user_num: the userID parameter of the tweet object.
    :param dataset: can either be "follows.csv" or "follows_sample.csv"
    for testing purposes
    :return: a list of userID that follows user_num
    """

    with open(dataset, "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)

        for line in reader:
            # the user of line[1] is followed by the userID of <line[0]>
            r.lpush(f"followees{line[1]}", line[0])

    ls_of_followers = r.lrange(f'followees{user_num}', 0, -1)
    return ls_of_followers


def getTimeline(user_num):
    """
    :param user_num: the userID parameter of the tweet object.
    :return: a list containing 10 tweet objects that are from user_num's timeline
    """
    tweet_obj_ls = []

    for i in r.lrange(f'timeline{user_num}', 0, -1)[:10]:
        timeline = r.hgetall(f"tweet{i}")
        timeline_tweet = Tweet(timeline['tweet_id'],
                               timeline['user_id'],
                               timeline['tweet_ts'],
                               timeline['tweet_text'])
        tweet_obj_ls.append(timeline_tweet)

    return tweet_obj_ls
