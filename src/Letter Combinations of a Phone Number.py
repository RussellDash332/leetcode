class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        q = keyboard[digits[0]]
        for i in digits[1:]:
            if i == "1": continue
            else:
                q2 = []
                for j in q:
                    for k in keyboard[i]: q2.append(j+k)
                q = q2
        return q