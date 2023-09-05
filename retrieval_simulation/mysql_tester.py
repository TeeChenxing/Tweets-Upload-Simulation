import mysql.connector
import mysql_driver as driver
import mysql_twitterAPI as twAPI
import pprint as pp


def main():

    tweets_api = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='dualSQL_admin',
                                         database='tweets_db')

    mycursor = tweets_api.cursor()

    wanted_userID = 3
    limit = 10

    # this is commented out due to how long it takes to actually run on my PC
    # post_tweet_time = driver.post_tweet_timer("tweet.csv", mycursor, tweets_api)
    # get_timeline_time = driver.find_timeline_timer(mycursor, limit)
    # print(f'Tweets per Second: {7 / post_tweet_time}')
    # print(f'Timelines per Second: {100 / get_timeline_time}')

    """
    I have decided that these functions return a dataframe instead of a list because it is much easier to 
    read than a gigantic list of information. User can simply convert a dataframe column into a list if
    they so desire. 
    """

    timeline_df = twAPI.get_timeline(mycursor, wanted_userID, limit)
    print(f"These are the tweets from user number: {wanted_userID}'s timeline")
    pp.pprint(timeline_df)
    print()

    followers_df = twAPI.get_followers(mycursor, wanted_userID)
    print(f"These are the user IDs of the people who follows user {wanted_userID}.")
    pp.pprint(followers_df)
    print()

    followees_df = twAPI.get_followees(mycursor, wanted_userID)
    print(f"These are the User IDs of the people who user {wanted_userID} follows.")
    pp.pprint(followees_df)
    print()

    tweets_df = twAPI.get_tweets(mycursor, wanted_userID)
    print(f"These are the tweets from user {wanted_userID}.")
    pp.pprint(tweets_df)
    print()


if __name__ == '__main__':
    main()
