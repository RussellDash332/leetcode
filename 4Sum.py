class Solution(object):    
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
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
            if 2 * h > target:
                break
            if target - h in pairs:
                for na, nb in pairs[h]:
                    for nc, nd in pairs[target - h]:
                        if na == nb == nc == nd:
                            if freq[na] >= 4:
                                res.add((na, nb, nc, nd)) # 1111
                        else: # na != nd
                            naa, nbb, ncc, ndd = sorted((na, nb, nc, nd))
                            if naa == nbb:
                                if freq[naa] >= 2:
                                    if naa == ncc:
                                        if freq[naa] >= 3:
                                            res.add((naa, nbb, ncc, ndd)) # 1112
                                    elif ncc == ndd:
                                        if freq[ncc] >= 2:
                                            res.add((naa, nbb, ncc, ndd)) # 1122
                                    else:
                                        res.add((naa, nbb, ncc, ndd)) # 1123
                            else:
                                if nbb == ncc:
                                    if freq[nbb] >= 2:
                                        if ncc == ndd:
                                            if freq[nbb] >= 3:
                                                res.add((naa, nbb, ncc, ndd)) # 1222
                                        else:
                                            res.add((naa, nbb, ncc, ndd)) # 1223
                                else:
                                    if ncc == ndd:
                                        if freq[ncc] >= 2:
                                            res.add((naa, nbb, ncc, ndd)) # 1233
                                    else:
                                        res.add((naa, nbb, ncc, ndd)) # 1234
        return res
