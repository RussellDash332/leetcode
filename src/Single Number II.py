class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        offset = min(nums)
        
        def base2(n):
            res = []
            while n:
                res.append(n % 2)
                n //= 2
            while len(res) != 32:
                res.append(0)
            return res

        res = [0] * 32
        for i in nums:
            i = base2(i - offset)
            for j in range(32):
                res[j] = (res[j] + i[j]) % 3
        
        ans = 0
        for i in range(1, 33):
            ans *= 2
            ans += res[-i]
        return ans + offset
