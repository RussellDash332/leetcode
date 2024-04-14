# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            ll = ListNode(None) # dummy head
            ptr = ll
            ptr1, ptr2 = lists[0], lists[1]
            while ptr1 and ptr2:
                if ptr1.val <= ptr2.val:
                    ptr.next = ptr1
                    ptr1 = ptr1.next
                else:
                    ptr.next = ptr2
                    ptr2 = ptr2.next
                ptr = ptr.next
            while ptr1:
                ptr.next = ptr1
                ptr1 = ptr1.next
                ptr = ptr.next
            while ptr2:
                ptr.next = ptr2
                ptr2 = ptr2.next
                ptr = ptr.next
            return ll.next
        
        res = []
        for i in range(len(lists) // 2 + 1):
            res.append(self.mergeKLists(lists[2*i:2*(i+1)]))
        return self.mergeKLists(res)
