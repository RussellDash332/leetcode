from random import choice

class RandomizedCollection:

    def __init__(self):
        self.ms = set()
        self.hm = {}
        self.prev = None
        self.cache = None

    def insert(self, val: int) -> bool:
        can = (val, 1) not in self.ms
        if can: self.hm[val] = 0
        self.hm[val] += 1
        self.ms.add((val, self.hm[val]))
        self.prev = 1
        return can

    def remove(self, val: int) -> bool:
        can = (val, 1) in self.ms
        if can:
            self.ms.remove((val, self.hm[val]))
            self.hm[val] -= 1
        self.prev = 2
        return can

    def getRandom(self) -> int:
        if self.prev != 3: self.cache = list(self.ms)
        self.prev = 3
        return choice(self.cache)[0]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
