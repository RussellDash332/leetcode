# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        sz = 0
        while curr != None:
            curr = curr.next
            sz += 1
        curr = head
        for _ in range(sz // 2):
            curr = curr.next
        return curr
