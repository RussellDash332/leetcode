class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def helper(weights, days, capacity):
            t_days = 1
            s = 0
            
            for w in weights:
                s += w
                if s > capacity:
                    t_days += 1
                    s = w
                    
                if t_days > days:
                    return False
                
            return True
        
        min_w = max(weights)
        max_w = sum(weights)
        
        ans = -1
        while min_w <= max_w:
            mid = (min_w + max_w)//2
            if helper(weights, days, mid):
                ans = mid
                max_w = mid - 1
            else:
                min_w = mid + 1
                
        return ans
