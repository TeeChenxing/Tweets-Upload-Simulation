import twitterAPI as twAPI
import redis
import driver as driver
r = redis.Redis('localhost', 6379, decode_responses=True)


def main():

    r.flushall()

    user_number = 1
    x = 1000

    follow_ls = twAPI.follows(user_number, "follows.csv")
    print(f"User {user_number} follows these users: {follow_ls}")
    print()

    followers_ls = twAPI.followees(user_number, "follows.csv")
    print(f"User {user_number} is followed by these users: {followers_ls}")
    print()

    post_tweet_time = driver.postTweetTimer("tweets.csv")
    print("Post Tweet Elapsed Time: ", post_tweet_time)

    timeline_time = driver.getTimelineTimer()
    print("Timeline Elapsed Time: ", timeline_time)

    test_timeline = twAPI.getTimeline(user_number)
    for obj in test_timeline:
        print(obj)


main()