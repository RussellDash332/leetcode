class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = {}
        prev = ptr = mcnt = best = 0
        while ptr < len(s):
            if s[ptr] not in cnt:
                cnt[s[ptr]] = 0
            cnt[s[ptr]] += 1
            mcnt = max(mcnt, cnt[s[ptr]])
            ptr += 1
            if ptr - mcnt - prev <= k:
                best = max(best, ptr - prev)
            else:
                cnt[s[prev]] -= 1
                prev += 1

        return best
