class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        for i in nums: s ^= i
        bk = bin(k)[2:]
        bs = bin(s)[2:]
        m = max(len(bk), len(bs))
        bk, bs = bk.zfill(m), bs.zfill(m)
        return sum(bk[i]!=bs[i] for i in range(m))