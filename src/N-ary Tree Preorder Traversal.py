"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def preorder(node):
            if not node: return
            result.append(node.val)
            for children in node.children:
                preorder(children)
        preorder(root)
        return result
