# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(p, q):
            if not p and not q: return True
            if not p and q: return False
            if p and not q: return False
            if p.val != q.val: return False
            return helper(p.left, q.right) and helper(p.right, q.left)
        return helper(root.left, root.right)
