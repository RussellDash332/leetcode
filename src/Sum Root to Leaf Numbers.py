# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def helper(v, c):
            if v == None: return
            if v.left == v.right == None: ans[0] += 10*c+v.val; return
            helper(v.left, 10*c+v.val)
            helper(v.right, 10*c+v.val)
        helper(root, 0)
        return ans[0]