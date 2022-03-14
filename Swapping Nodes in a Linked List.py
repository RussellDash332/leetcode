# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        sz = 0
        while curr != None:
            curr = curr.next
            sz += 1
        s1, s2 = head, head
        for _ in range(k - 1):
            s1 = s1.next
        for _ in range(sz - k):
            s2 = s2.next
        s1.val, s2.val = s2.val, s1.val
        return head
