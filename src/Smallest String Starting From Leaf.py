# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(v, t):
            s = chr(v.val+97)+t
            if v.left and v.right: return min(helper(v.left, s), helper(v.right, s))
            elif v.left: return helper(v.left, s)
            elif v.right: return helper(v.right, s)
            else: return s
        return helper(root, '')