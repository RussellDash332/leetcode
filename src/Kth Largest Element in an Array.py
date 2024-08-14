class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def helper(nums, k):
            l, r, m = [], [], []
            c = randint(0, len(nums)-1)
            for i in range(len(nums)):
                (l if nums[i] < nums[c] else r if nums[i] > nums[c] else m).append(nums[i])
            if len(r)+1 <= k <= len(r)+len(m): return nums[c]
            elif len(r)+len(m) < k: return helper(l, k-len(r)-len(m))
            return helper(r, k)
        return helper(nums, k)