from math import *
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        a = [nums[0]]
        for i in nums[1:]:
            a.append(i)
            while len(a)>1 and gcd(a[-1], a[-2]) > 1: a.append(lcm(a.pop(), a.pop()))
        return a