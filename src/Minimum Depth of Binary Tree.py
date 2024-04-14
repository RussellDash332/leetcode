# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        best = 10**5 + 1
        def trav(pt, d=1):
            nonlocal best
            if not pt: return
            if not pt.left and not pt.right:
                best = min(best, d)
            trav(pt.left, d+1)
            trav(pt.right, d+1)
        trav(root)
        return best
