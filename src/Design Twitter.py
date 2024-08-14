from heapq import *
class Twitter(object):

    def __init__(self):
        self.p = {}
        self.f = {}
        self.t = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.p: self.p[userId] = []
        self.p[userId].append((self.t, tweetId))
        self.t -= 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        q = []
        for t in self.p.get(userId, []): q.append(t)
        for v in self.f.get(userId, []):
            for t in self.p.get(v, []): q.append(t)
        heapify(q); r = []
        while q and len(r) < 10: r.append(heappop(q)[1])
        return r

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.f: self.f[followerId] = set()
        self.f[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.f: self.f[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)