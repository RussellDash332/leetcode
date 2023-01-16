class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f, z = 1, 0
        for i in nums:
            if i == 0: z += 1
            else: f *= i
        res = []
        for i in nums:
            if z == 1:
                if i: res.append(0)
                else: res.append(f)
            elif z: res.append(0)
            else: res.append(f//i)
        return res
