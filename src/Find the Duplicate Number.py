class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Floyd's tortoise and hare
        t, h = nums[0], nums[0]
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h:
                break
        p = nums[0]
        while p != t:
            p, t = nums[p], nums[t]
        return p
