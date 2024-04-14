# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t, h = head, head
        while t and h:
            t = t.next
            if h and h.next:    h = h.next.next
            else:               break
            if t == h:          break
        if t != h: return
        t = head
        while t != h:
            t, h = t.next, h.next
        return t
