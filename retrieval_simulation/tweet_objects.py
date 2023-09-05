class Tweet:

    def __init__(self, tweetID, userID, tweetTXT, tweetTime):
        self.tweetID = tweetID
        self.userID = userID
        self.tweetTXT = tweetTXT
        self.tweetTime = tweetTime

    def __str__(self):
        return f"Tweet: {self.tweetID}, {self.userID}, {self.tweetTime}, '{self.tweetTXT}')"
