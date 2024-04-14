class WordDictionary(object):

    def __init__(self):
        self.t = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        ptr = self.t
        for i in word + '!':
            if i not in ptr:
                ptr[i] = {}
            ptr = ptr[i]

    def search(self, word, idx=0, ptr=None):
        """
        :type word: str
        :rtype: bool
        """
        if idx == len(word): return '!' in ptr
        if ptr == None:
            ptr = self.t
        if word[idx] == '.':
            for k, v in ptr.items():
                if k != '!' and self.search(word, idx+1, v):
                    return True
        if word[idx] not in ptr: return False
        return self.search(word, idx+1, ptr[word[idx]])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
