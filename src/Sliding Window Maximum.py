class Solution(object):
    from collections import deque
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        w = deque(); ans = []
        for i in range(len(nums)):
            while w and w[-1][0] <= nums[i]: w.pop()
            w.append((nums[i], i))
            while w[0][1] <= i-k: w.popleft()
            if i+1 >= k: ans.append(w[0][0])
        return ans