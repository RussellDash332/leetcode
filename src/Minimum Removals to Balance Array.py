class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort(); n = len(nums); z = r = 0
        for i in range(n):
            while r < n and nums[r] <= nums[i]*k: r += 1
            z = max(z, r-i)
        return n-z
