class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f, z = 1, 0
        for i in nums:
            if i == 0: z += 1
            else: f *= i
        res = []
        for i in nums:
            if z > 1 or (z==1 and i): res.append(0)
            elif i: res.append(f//i)
            else: res.append(f)
        return res
