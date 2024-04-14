# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        sz = 0
        while curr != None:
            curr = curr.next
            sz += 1
        curr = head
        if n == sz:
            return head.next
        elif n == 1:
            for _ in range(sz - 2):
                curr = curr.next
            curr.next = None
            return head
        else:
            for _ in range(sz - n - 1):
                curr = curr.next
            prev = curr
            succ = curr.next.next
            prev.next = succ
            return head
