class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        pairs = {}
        num_keys = sorted(freq.keys())
        for i in range(len(num_keys)):
            for j in range(i, len(num_keys)):
                k, l = num_keys[i], num_keys[j]
                if k + l not in pairs:
                    pairs[k + l] = []
                pairs[k + l].append((k, l))
        res = set()
        pairs_keys = sorted(pairs.keys())
        for h in pairs_keys:
            if 2 * h > 0:
                break
            if -h in freq:
                for na, nb in pairs[h]:
                    nc = -h
                    if na == nb == nc:
                        if freq[na] >= 3:
                            res.add((na, nb, nc)) # 111
                    else: # na != nc
                        naa, nbb, ncc = sorted((na, nb, nc))
                        if naa == nbb:
                            if freq[naa] >= 2:
                                res.add((naa, nbb, ncc)) # 112
                        else:
                            if nbb == ncc:
                                if freq[nbb] >= 2:
                                    res.add((naa, nbb, ncc)) # 122
                            else:
                                res.add((naa, nbb, ncc))
        return res
