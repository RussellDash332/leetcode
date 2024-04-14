class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def upper_bound(sub, idx):
            lo, hi = 0, len(sub) - 1
            while hi > lo:
                mid = (lo + hi) // 2
                if nums[sub[mid]] < nums[idx]:
                    lo = mid + 1
                else:
                    hi = mid
            return hi

        temp = []
        par = [None] * len(nums)

        for i in range(len(nums)):
            if not temp or nums[i] > nums[temp[-1]]:
                if temp:
                    par[i] = temp[-1]
                temp.append(i)
            else:
                rep = upper_bound(temp, i)
                temp[rep] = i
                if rep != 0:
                    par[i] = temp[rep - 1]

        final = []
        curr = temp[-1]
        while curr != None:
            final.append(curr)
            curr = par[curr]
        return len(final)
