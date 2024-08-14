# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def helper(v, d):
            if d == len(ans): ans.append(v.val)
            if v.right: helper(v.right, d+1)
            if v.left: helper(v.left, d+1)
        if root: helper(root, 0)
        return ans