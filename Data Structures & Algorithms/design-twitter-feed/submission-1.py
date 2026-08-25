import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0  # global timestamp
        self.tweets = defaultdict(list)  # userId -> list of (time, tweetId)
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append tweet with timestamp
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # Collect tweets from user and followees
        feed = []
        users = self.following[userId] | {userId}
        for u in users:
            for t in self.tweets[u][-10:]:  # only last 10 tweets per user
                feed.append(t)
        # Get 10 most recent tweets overall
        return [tweetId for _, tweetId in heapq.nlargest(10, feed)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
