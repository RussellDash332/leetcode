class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0; nums.insert(0, 1)
        while len(nums) > 2:
            if nums[-1] >= nums[-2]: nums.pop()
            else:
                b = (nums[-2]+nums[-1]-1)//nums[-1]
                c = nums[-2]//b
                nums.pop(), nums.pop(), nums.append(c)
                ans += b-1
        return ans
