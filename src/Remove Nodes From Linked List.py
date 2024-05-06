# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s = [(head.val, 0)]; ptr = head.next
        r = [0]
        while ptr:
            r.append(0)
            while s and s[-1][0] < ptr.val:
                r[s.pop()[1]] = 1
            s.append((ptr.val, len(r)-1))
            ptr = ptr.next
        s.reverse(); p = 0; ll = ListNode(-1); cur = head; llp = ll
        while s:
            if p == s[-1][1]: llp.next = ListNode(s.pop()[0]); llp = llp.next
            cur = cur.next; p += 1
        return ll.next