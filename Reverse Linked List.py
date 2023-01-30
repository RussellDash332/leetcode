# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        curr, nxt = head, head.next
        while nxt:
            curr2, nxt2 = nxt, nxt.next
            nxt.next = curr
            curr, nxt = curr2, nxt2
        head.next = None
        return curr
