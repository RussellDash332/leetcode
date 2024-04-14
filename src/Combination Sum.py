class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        candidates.sort(reverse=True)
        def bt(idx, target, curr):
            if target == 0: return res.add(tuple(curr))
            if idx == len(candidates) or target < 0: return
            bt(idx+1, target, curr)
            bt(idx, target-candidates[idx], curr + [candidates[idx]])
        bt(0, target, [])
        return list(map(list, res))
