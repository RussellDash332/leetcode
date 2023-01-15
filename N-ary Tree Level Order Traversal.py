"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = [[] for _ in range(1001)]
        def preorder(node, depth=0):
            if not node: return
            levels[depth].append(node.val)
            for children in node.children:
                preorder(children, depth+1)
        preorder(root)
        while levels and levels[-1] == []:
            levels.pop()
        return levels
