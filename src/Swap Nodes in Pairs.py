# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        sz = 0
        while curr != None:
            curr = curr.next
            sz += 1
        try:
            l, r = head, head.next
            for _ in range(sz // 2):
                l.val, r.val = r.val, l.val
                try:
                    l, r = l.next.next, r.next.next
                except:
                    break
        except:
            pass
        return head
