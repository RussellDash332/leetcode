from random import choice

class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        can = val not in self.set
        self.set.add(val)
        return can

    def remove(self, val: int) -> bool:
        can = val in self.set
        if can: self.set.remove(val)
        return can

    def getRandom(self) -> int:
        return choice(list(self.set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
