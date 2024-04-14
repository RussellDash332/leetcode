# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def update_height(self, root):
        if not root: return 0
        h = 1 + max(self.update_height(root.left), self.update_height(root.right))
        root.height = h
        return h

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.update_height(root)
        def helper(pt):
            if not pt: return True
            if pt.left and pt.right and not (-1 <= pt.left.height - pt.right.height <= 1):
                return False
            elif pt.left and not pt.right and pt.left.height > 1:
                return False
            elif pt.right and not pt.left and pt.right.height > 1:
                return False
            return helper(pt.left) and helper(pt.right)
        return helper(root)
