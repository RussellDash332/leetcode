# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return
        val = postorder[-1]
        idx = inorder.index(val)
        return TreeNode(
            val,
            self.buildTree(inorder[:idx], postorder[:idx]),
            self.buildTree(inorder[idx+1:], postorder[idx:-1])
        )
