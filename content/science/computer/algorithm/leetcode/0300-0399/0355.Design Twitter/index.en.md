---
title: 0355.Design Twitter
date: 2026-09-18
---

## Solution

```python
from collections import defaultdict
from heapq import nlargest
from typing import List

class Twitter:
    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_following = defaultdict(set)
        self.tweets = dict()
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append(tweetId)
        self.tweets[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.user_following[userId]
        users = set(following)
        users.add(userId)
        tweets = [self.user_tweets[u][::-1][:10] for u in users]
        tweets = sum(tweets, [])
        return nlargest(10, tweets, key=lambda tweet: self.tweets[tweet])

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        following = self.user_following[followerId]
        if followeeId in following:
            following.remove(followeeId)

# 本地测试
if __name__ == "__main__":
    obj = Twitter()
    obj.postTweet(1,5)
    print(obj.getNewsFeed(1)) # [5]
    obj.follow(1,2)
    obj.postTweet(2,6)
    print(obj.getNewsFeed(1)) # [6,5]
    obj.unfollow(1,2)
    print(obj.getNewsFeed(1)) # [5]
```
