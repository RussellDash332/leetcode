class SmallestInfiniteSet:

    def __init__(self):
        self.mex = set()

    def popSmallest(self) -> int:
        i = 1
        while i in self.mex: i += 1
        self.mex.add(i)
        return i

    def addBack(self, num: int) -> None:
        self.mex.discard(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)