"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        ptr = head
        while ptr:
            ptr.copy = Node(ptr.val, ptr.next, ptr.random)
            ptr = ptr.next
        ptr = head
        while ptr:
            if ptr.next: ptr.copy.next = ptr.next.copy
            if ptr.random: ptr.copy.random = ptr.random.copy
            ptr = ptr.next
        return head.copy if head else None