class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        s = sorted(nums)
        return max(s[i]+s[len(s)-1-i] for i in range(len(s)//2))