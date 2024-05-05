# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ptr = node
        while ptr.next != None:
            ptr.val, ptr.next.val = ptr.next.val, ptr.val
            if ptr.next.next == None: ptr.next = None; break
            ptr = ptr.next