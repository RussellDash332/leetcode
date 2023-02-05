# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.h = {}

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if root in self.h: return self.h[root]
        def helper(t):
            ans = 0
            if t.left:
                ans += self.rob(t.left.left) + self.rob(t.left.right)
            if t.right:
                ans += self.rob(t.right.left) + self.rob(t.right.right)
            return ans
        res = max(self.rob(root.left) + self.rob(root.right), root.val + helper(root))
        self.h[root] = res
        return res
