# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(l, r):
            if l > r: return
            mi = (l+r)//2
            root = TreeNode(nums[mi])
            root.left = helper(l, mi-1)
            root.right = helper(mi+1, r)
            return root
        return helper(0, len(nums)-1)
