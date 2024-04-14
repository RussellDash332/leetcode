"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def postorder(node):
            if not node: return
            for children in node.children:
                postorder(children)
            result.append(node.val)
        postorder(root)
        return result
