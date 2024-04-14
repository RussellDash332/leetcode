# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2 = "", ""
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        n = int(n1[::-1]) + int(n2[::-1])

        result = ListNode()
        curr = result
        
        if n < 10:
            return ListNode(n)
        
        print(n)
        
        while n >= 10:
            curr.val = n % 10
            n //= 10
            if n < 10:
                curr.next = ListNode(n)
                break
            else:
                curr.next = ListNode()
                curr = curr.next
        return result
