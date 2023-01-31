class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums)-1
        while goal != 0:
            can = False
            for i in range(1, goal+1):
                if nums[goal-i] >= i:
                    goal -= i
                    can = True
                    break
            if not can: return False
        return True

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        goal = n-1
        for i in range(1, goal+1):
            if nums[-i-1] + n-i-1 >= goal:
                goal = n-i-1
        return not goal
