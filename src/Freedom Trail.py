class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        h = {}
        for i in range(len(ring)):
            if ring[i] not in h: h[ring[i]] = []
            h[ring[i]].append(i)
        dp = [10000]*len(ring)
        for i in h[key[0]]: dp[i] = min(i%len(ring), -i%len(ring))
        for i in range(1, len(key)):
            tmp = [10000]*len(ring)
            for j in h[key[i]]: tmp[j] = min(dp[k]+min((j-k)%len(ring), (k-j)%len(ring)) for k in h[key[i-1]])
            dp = tmp
        return min(dp)+len(key)