# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(v, k):
            if not v: return 0
            m = max(k, v.val)
            return (v.val == m) + helper(v.left, m) + helper(v.right, m)
        return helper(root, root.val)