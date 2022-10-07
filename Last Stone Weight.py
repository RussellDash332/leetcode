class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) != 1:
            stones.sort()
            stones.append(abs(stones.pop() - stones.pop()))
        return stones[0]
