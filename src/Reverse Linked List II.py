# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """ 
        if not head or not head.next or left == right: return head
        ptr, prev = head, None
        for _ in range(left-1): ptr, prev = ptr.next, ptr
        start = ptr
        curr, nxt = ptr, ptr.next
        for _ in range(right-left):
            curr2, nxt2 = nxt, nxt.next
            nxt.next = curr
            curr, nxt = curr2, nxt2
        if prev:
            prev.next = curr
        if start:
            start.next = nxt
        if start != head:
            return head
        else: # prev is None
            return curr
