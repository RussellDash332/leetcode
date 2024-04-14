class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(str(int(''.join(list(map(str, digits)))) + 1))
