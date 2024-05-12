import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(
            list)  # user_id -> list of [count, tweet_ids]
        self.follow_map = defaultdict(set)  # userId -> set of followees

    def post(self, user_id: int, tweet_id: int) -> None:
        self.tweet_map[user_id].append([self.count, tweet_id])
        self.count -= 1

    def get_news_feed(self, user_id: int) -> list[int]:
        res = []
        min_heap = []

        self.follow_map[user_id].add(user_id)
        for followee_id in self.follow_map[user_id]:
            if followee_id in self.tweet_map:
                index = len(self.tweet_map[followee_id]) - 1
                count, tweetId = self.tweet_map[followee_id][index]
                heapq.heappush(min_heap,
                               [count, tweetId, followee_id, index - 1])

        while min_heap and len(res) < 10:
            count, tweetId, followee_id, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followee_id][index]
                heapq.heappush(min_heap,
                               [count, tweetId, followee_id, index - 1])
        return res

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.follow_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.follow_map[follower_id]:
            self.follow_map[follower_id].remove(followee_id)


# Usage example:
twitter = Twitter()
twitter.post(0)
twitter.follow(0, 1)
twitter.get_news_feed(0)
