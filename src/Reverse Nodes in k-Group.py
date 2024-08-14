# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        base = nxt = ListNode()
        base.next = l = r = head
        while True:
            c = 0
            while r and c < k:
                r = r.next; c += 1
            if c == k:
                p, v = r, l # 3, 1 or 5, 3
                for _ in range(k): v.next, v, p = p, v.next, v
                nxt.next, nxt, l = p, l, r
            else:
                return base.next