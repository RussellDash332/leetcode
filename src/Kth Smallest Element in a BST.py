# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def update_size(self, root):
        if not root: return 0
        sz = 1 + self.update_size(root.left) + self.update_size(root.right)
        root.size = sz
        return sz

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.update_size(root)
        def helper(t, k):
            if (t.left == None and k == 1):
                return t
            elif (t.left == None and k > 1):
                return helper(t.right, k - 1)
            elif (t.left != None and t.left.size + 1 == k):
                return t
            elif (t.left != None and k > t.left.size + 1):
                return helper(t.right, k - t.left.size - 1)
            else:
                return helper(t.left, k)
        return helper(root, k).val
