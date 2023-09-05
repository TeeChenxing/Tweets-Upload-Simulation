import mysql.connector
import mysql_driver as driver1
import mysql_twitterAPI as twAPI1
import redis_twitterAPI as twAPI2
import redis
import redis_driver as driver2
import os

r = redis.Redis('localhost', 6379, decode_responses=True)
data_folder = "datasets"

follows_path = os.path.join(data_folder, "follows.csv")
tweets_path = os.path.join(data_folder, "tweets.csv")


def sql_runtime():
    tweets_api = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='dualSQL_admin',
                                         database='tweets_db')

    mycursor = tweets_api.cursor(buffered=True)
    limit = 10

    post_tweet_time = driver1.post_tweet_timer(
        tweets_path, mycursor, tweets_api)
    get_timeline_time = driver1.find_timeline_timer(mycursor, limit)
    print(f'Time to Post all Tweets Using MySQL: {post_tweet_time}')
    print()
    print(f'Timelines per Second Using MySQL: {100 / get_timeline_time}')
    print()


def redis_runtime():
    r.flushall()
    x = 1000

    post_tweet_time = driver2.postTweetTimer(tweets_path)
    timeline_time = driver2.getTimelineTimer(x)
    print(f'Time to Post all Tweets Using Redis: {post_tweet_time}')
    print()
    print(f'Timelines per Second Using Redis: {1000 / timeline_time}')


def main():
    sql_runtime()
    redis_runtime()


if __name__ == '__main__':
    main()
