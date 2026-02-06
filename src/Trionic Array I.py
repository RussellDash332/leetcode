class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        NUMS = [[]]
        result = -float('inf')
        for i in nums:
            if not NUMS[-1] or NUMS[-1][-1] != i: NUMS[-1].append(i)
            else: return False
        for nums in NUMS:
            n = len(nums)
            peaks = [i for i in range(1, n-1) if nums[i]>max(nums[i-1],nums[i+1])]
            troughs = [i for i in range(1, n-1) if nums[i]<min(nums[i-1],nums[i+1])]
            return len(peaks) == len(troughs) == 1 and nums[0] < nums[1] and nums[-2] < nums[-1]