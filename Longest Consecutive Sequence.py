class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        lo = min(nums)
        nums = list(map(lambda x: str(x-lo).zfill(10), set(nums)))
        for i in range(10):
            buckets = []
            for _ in range(10):
                buckets.append([])
            for j in nums:
                buckets[int(j[-i-1])].append(j)
            nums.clear()
            for b in buckets:
                nums.extend(b)
        nums = list(map(int, nums))
        curr_el, curr_cnt = -1, 0
        best = 0
        for i in nums:
            if curr_el + 1 == i:
                curr_cnt += 1
            else:
                best = max(best, curr_cnt)
                curr_cnt = 1
            curr_el = i
        return max(best, curr_cnt)
