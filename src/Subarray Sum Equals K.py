class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        d, p = {0: 1}, 0

        for el in nums:
            p += el
            if p - k in d:
                ans += d[p - k]
            if p not in d:
                d[p] = 0
            d[p] += 1
        return ans
