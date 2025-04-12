from collections import defaultdict, deque
from typing import List
from heapq import heappush, heappop


class Twitter:
    def __init__(self):
        self._user_tweet = defaultdict(deque)
        self._follower_followee = defaultdict(set)
        self._tweet_order = 0
        self._MAX_FEED_COUNT = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._user_tweet[userId].appendleft((self._tweet_order, tweetId))
        self._tweet_order += 1
        if len(self._user_tweet[userId]) > self._MAX_FEED_COUNT:
            self._user_tweet[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        return self._getNews_MinHeapApproach(userId)


    def follow(self, followerId: int, followeeId: int) -> None:
        self._follower_followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._follower_followee[followerId].discard(followeeId)

    def _getNews_MergeSortedListsApproach(self, userId: int) -> List[int]:
        maxOrderHeap = []
        self.follow(userId, userId)
        for usrId in self._follower_followee[userId]:
            tweets = self._user_tweet[usrId]
            if not tweets:
                continue
            tweetIndex = 0
            tweetOrder, tweetId = tweets[tweetIndex]
            heappush(maxOrderHeap, (-tweetOrder, usrId, tweetIndex, tweetId))
        newsFeed = []
        while maxOrderHeap and len(newsFeed) < self._MAX_FEED_COUNT:
            order, usrId, tweetIndex, tweetId = heappop(maxOrderHeap)
            newsFeed.append(tweetId)
            if tweetIndex < len(self._user_tweet[usrId]) - 1:
                order, tweetId = self._user_tweet[usrId][tweetIndex+1]
                heappush(maxOrderHeap, (-order, usrId, tweetIndex+1, tweetId))
        return newsFeed

    def _getNews_MinHeapApproach(self, userId:int)-> List[int]:
        minOrderHeap = []
        self.follow(userId, userId)
        for usrId in self._follower_followee[userId]:
            for tweet in self._user_tweet[usrId]:
                heappush(minOrderHeap, tweet)
                if len(minOrderHeap) > self._MAX_FEED_COUNT:
                    heappop(minOrderHeap)
        newsFeed = deque()
        while minOrderHeap:
            _, tweetId = heappop(minOrderHeap)
            newsFeed.appendleft(tweetId)
        return list(newsFeed)