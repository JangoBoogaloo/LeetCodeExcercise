from collections import defaultdict, deque
from typing import List
from heapq import heappush, heappop, heapify


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
        news_pq = []
        for tweet in self._user_tweet[userId]:
            heappush(news_pq, tweet)
        for followee in self._follower_followee[userId]:
            for tweet in self._user_tweet[followee]:
                heappush(news_pq, tweet)
                if len(news_pq) > self._MAX_FEED_COUNT:
                    heappop(news_pq)
        answer = deque()
        while news_pq:
            _, tweetId = heappop(news_pq)
            answer.appendleft(tweetId)
        return list(answer)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self._follower_followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followerId not in self._follower_followee:
            return
        self._follower_followee[followerId].remove(followeeId)
