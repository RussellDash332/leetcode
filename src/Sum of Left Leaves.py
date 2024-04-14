# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node, dr):
            if node == None: return 0
            if node.left == node.right == None and dr == 1: return node.val
            return helper(node.left, 1) + helper(node.right, 0)
        return helper(root, 0)