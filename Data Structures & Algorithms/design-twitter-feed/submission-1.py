class Twitter:

    def __init__(self):
        self.tweets = []
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        '''
        tweets should be tuples (user, tweetId)
        '''
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        initialize n = 10
        dummy = self.tweets
        - while self.tweets and n > 10:
            - user, tweet = self.tweets.pop()
            - check if userId == user or user in following[userId]:
                if true, append to our result and decrement n
                else:
                    continue
        '''
        result = []
        tweets = self.tweets[:]
        print(self.tweets)
        n = 10
        while tweets and n > 0:
            user, tweet = tweets.pop()
            if userId == user or user in self.following[userId]:
                result.append(tweet)
                n -= 1

        print(self.tweets)
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
