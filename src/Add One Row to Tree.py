# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        def helper(v, d):
            if v == None:
                return
            if d == depth-1:
                v.left = TreeNode(val, left=v.left)
                v.right = TreeNode(val, right=v.right)
                return
            else:
                helper(v.left, d+1)
                helper(v.right, d+1)
        helper(root, 1)
        return root