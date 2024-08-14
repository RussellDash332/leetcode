class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        f = c = 0
        for p, s in sorted(zip(position, speed), reverse=1):
            u = float(target-p)/s
            if u > c: f += 1; c = u
        return f