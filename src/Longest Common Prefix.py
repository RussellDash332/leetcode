class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = []
        for i in range(min(map(len, strs))):
            if len({s[i] for s in strs}) != 1: break
            p.append(strs[0][i])
        return ''.join(p)
