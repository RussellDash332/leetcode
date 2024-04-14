# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr = ListNode(None)
        head2 = curr
        curr.next = head
        while curr:
            try:
                while curr.next.val == val:
                    curr.next = curr.next.next
            except:
                break
            curr = curr.next
        return head2.next
