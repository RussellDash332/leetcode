class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        (s1, e1), (s2, e2) = event1, event2
        return s1 <= s2 <= e1 or s2 <= s1 <= e2
