class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        intiution 2:
        when posting new post, posts[userId].append(timestamp,post)
        for followee in following[userId]:
            heap.append(posts[followee])
        '''
        heap = []
        result = []
        for post in self.tweets[userId]:
            heap.append(post)

        for followee in self.following[userId]:
            for post in self.tweets[followee]:
                heap.append(post)
        


        heapq.heapify(heap)
        while heap and len(result) < 10:
            timestamp, tweet = heapq.heappop(heap)
            if tweet not in result:
                result.append(tweet)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)




# class Twitter:

#     def __init__(self):
#         self.tweets = []
#         self.following = defaultdict(set)

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         '''
#         tweets should be tuples (user, tweetId)
#         '''
#         self.tweets.append((userId, tweetId))

#     def getNewsFeed(self, userId: int) -> List[int]:
#         '''
#         initialize n = 10
#         dummy = self.tweets
#         - while self.tweets and n > 10:
#             - user, tweet = self.tweets.pop()
#             - check if userId == user or user in following[userId]:
#                 if true, append to our result and decrement n
#                 else:
#                     continue
#         '''
#         # result = []
#         # tweets = self.tweets[:]
#         # n = 10
#         # while tweets and n > 0:
#         #     user, tweet = tweets.pop()
#         #     if userId == user or user in self.following[userId]:
#         #         result.append(tweet)
#         #         n -= 1

#         # return result

#         '''
#         intiution 2:
#         when posting new post, posts[userId].append(timestamp,post)
#         for followee in following[userId]:
#             heap.append(posts[followee])
#         '''

#     def follow(self, followerId: int, followeeId: int) -> None:
#         self.following[followerId].add(followeeId)

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         self.following[followerId].discard(followeeId)

