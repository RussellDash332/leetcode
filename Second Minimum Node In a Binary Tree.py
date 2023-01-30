# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        vals = set()
        def inorder(pt):
            if not pt: return
            inorder(pt.left)
            vals.add(pt.val)
            inorder(pt.right)
        inorder(root)
        vals.remove(min(vals))
        return min(vals) if vals else -1
