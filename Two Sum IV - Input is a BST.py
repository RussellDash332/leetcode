# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        inorder = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)
        helper(root)
        
        return self.twoSum(inorder, k)
        
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(numbers) - 1
        try:
            while numbers[lo] + numbers[hi] != target:
                if numbers[lo] + numbers[hi] > target:
                    hi -= 1
                else:
                    lo += 1
            return lo != hi
        except:
            return False
