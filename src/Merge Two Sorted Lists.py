# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lstres = []
        while l1 and l2:
            if l1.val < l2.val:
                lstres.append(l1.val)
                l1 = l1.next
            else:
                lstres.append(l2.val)
                l2 = l2.next
        while l1:
            lstres.append(l1.val)
            l1 = l1.next
        while l2:
            lstres.append(l2.val)
            l2 = l2.next
        
        if lstres:
            result = ListNode()
            curr = result
            for v in range(len(lstres)):
                curr.val = lstres[v]
                if v < len(lstres) - 1:
                    curr.next = ListNode()
                    curr = curr.next
            return result
        return None
