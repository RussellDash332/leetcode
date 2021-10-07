class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def helper(nums, m, cap):
            t_m = 1
            s = 0
            
            for n in nums:
                s += n
                if s > cap:
                    t_m += 1
                    s = n
                    
                if t_m > m:
                    return False
                
            return True
        
        min_n = max(nums)
        max_n = sum(nums)
        
        ans = -1
        while min_n <= max_n:
            mid = (min_n + max_n)//2
            if helper(nums, m, mid):
                ans = mid
                max_n = mid - 1
            else:
                min_n = mid + 1
                
        return ans
