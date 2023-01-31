class Trie(object):

    def __init__(self):
        self.t = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        ptr = self.t
        for i in word + '.':
            if i not in ptr:
                ptr[i] = {}
            ptr = ptr[i]

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ptr = self.t
        for i in word:
            if i not in ptr: return False
            ptr = ptr[i]
        return '.' in ptr

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        ptr = self.t
        for i in prefix:
            if i not in ptr: return False
            ptr = ptr[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
