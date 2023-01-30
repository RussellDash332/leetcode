# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return
        val = preorder[0]
        idx = inorder.index(val)
        return TreeNode(
            val,
            self.buildTree(preorder[1:idx+1], inorder[:idx]),
            self.buildTree(preorder[idx+1:], inorder[idx+1:])
        )
