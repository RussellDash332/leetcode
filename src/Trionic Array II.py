class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        NUMS = [[]]
        result = -float('inf')
        for i in nums:
            if not NUMS[-1] or NUMS[-1][-1] != i: NUMS[-1].append(i)
            else: NUMS.append([i])
        for nums in NUMS:
            n = len(nums)
            peaks = [i for i in range(1, n-1) if nums[i]>max(nums[i-1],nums[i+1])]
            troughs = [i for i in range(1, n-1) if nums[i]<min(nums[i-1],nums[i+1])]
            prev_p = n
            while troughs:
                t = troughs.pop(); t2 = t+1
                while peaks and peaks[-1] > t: prev_p = peaks.pop()
                if not peaks: break
                # add s[p..t] later
                p = peaks.pop(); p2 = p-1
                s = m = nums[p2]
                while True:
                    p2 -= 1
                    if p2 >= (troughs[-1] if troughs else 0):
                        s += nums[p2]
                        m = max(m, s)
                    else:
                        break
                s = m2 = nums[t2]
                while True:
                    t2 += 1
                    if t2 <= prev_p and t2 < n:
                        s += nums[t2]
                        m2 = max(m2, s)
                    else:
                        break
                prev_p = p
                #print(p, t, m, m2, peaks, troughs)
                result = max(result, m+m2+sum(nums[i] for i in range(p, t+1)))
        return result