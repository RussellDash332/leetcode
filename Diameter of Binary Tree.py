# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def update_height(self, root):
        if not root: return 0
        h = 1 + max(self.update_height(root.left), self.update_height(root.right))
        root.height = h
        return h

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.update_height(root)
        l = root.left.height if root.left else 0
        r = root.right.height if root.right else 0
        dl = self.diameterOfBinaryTree(root.left) if root.left else 0
        dr = self.diameterOfBinaryTree(root.right) if root.right else 0
        return max(l+r, dl, dr)
