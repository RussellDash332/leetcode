# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        r, c = 0, 0
        dr, dc = 0, 1
        done = set()
        while head:
            while 0 <= r < m and 0 <= c < n and (r, c) not in done:
                done.add((r, c))
                if not head: return matrix
                matrix[r][c] = head.val
                head = head.next
                r, c = r+dr, c+dc
            r, c = r-dr, c-dc
            dr, dc = dc, -dr
            r, c = r+dr, c+dc
        return matrix
