class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            t = tuple(sorted(s))
            if t not in h:
                h[t] = []
            h[t].append(s)
        return list(h.values())
