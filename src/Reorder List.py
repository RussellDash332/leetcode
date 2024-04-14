# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        from collections import deque
        ptr = head.next
        q = deque()
        while ptr:
            q.append(ptr)
            ptr = ptr.next
        t, prev = 1, head
        while q:
            if t % 2:   prev.next = q.pop()
            else:       prev.next = q.popleft()
            t, prev = 1-t, prev.next
        prev.next = None
