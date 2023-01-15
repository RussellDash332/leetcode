# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = [[] for _ in range(2001)]
        def preorder(node, depth=0):
            if not node: return
            levels[depth].append(node.val)
            preorder(node.left, depth+1)
            preorder(node.right, depth+1)
        preorder(root)
        while levels and levels[-1] == []:
            levels.pop()
        return [x[::(1-2*(i%2))] for i,x in enumerate(levels)]
