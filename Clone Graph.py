"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def __init__(self):
        self.g = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node:
            if node.val in self.g:
                return self.g[node.val]
            n = Node(node.val)
            self.g[n.val] = n
            u = []
            for nxt in node.neighbors:
                u.append(self.cloneGraph(nxt))
            n.neighbors = u
            return n
