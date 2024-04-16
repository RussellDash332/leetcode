class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        p = [s:=0]+[s:=s+i for i in nums]
        return [(2*i-len(nums))*nums[i]+(p[-1]-2*p[i]) for i in range(len(nums))]