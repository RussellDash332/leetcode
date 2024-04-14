from heapq import *

class MedianFinder(object):

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.left and num >= -self.left[0]:
            heappush(self.right, num)
        else:
            heappush(self.left, -num)
        while abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) < len(self.right):
                heappush(self.left, -heappop(self.right))
            else:
                heappush(self.right, -heappop(self.left))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2.0
        elif len(self.left) < len(self.right):
            return self.right[0]
        return -self.left[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
