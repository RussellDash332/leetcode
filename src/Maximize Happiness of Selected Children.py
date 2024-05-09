class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(); a = 0
        return sum(max(happiness.pop()-t, 0) for t in range(k))