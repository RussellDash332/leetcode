# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n = []; ptr = head
        while ptr: n.append(ptr.val); ptr = ptr.next
        s = 0
        for i in n: s = 10*s+i
        s *= 2
        m = n = None
        if s == 0: return ListNode(0)
        while s:
            m = ListNode(s%10); s //= 10; m.next = n; n = m
        return n