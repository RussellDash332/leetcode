class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        def bt(idx, target, curr):
            if idx == len(candidates) or target < 0: return
            if target == 0: res.add(tuple(curr))
            bt(idx+1, target, curr)
            bt(idx, target-candidates[idx], curr + [candidates[idx]])
        bt(0, target, [])
        return list(map(list, res))
