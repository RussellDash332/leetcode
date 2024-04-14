# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        sz = 0
        while curr != None:
            curr = curr.next
            sz += 1
        try:
            curr = head
            for _ in range(sz // 2 - 1):
                curr = curr.next
            curr.next = curr.next.next
        except:
            return None # one element is now gone
        return head
