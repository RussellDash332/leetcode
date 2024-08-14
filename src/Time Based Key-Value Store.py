class TimeMap(object):
    from bisect import bisect_right

    def __init__(self):
        self.m = {}
        self.v = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.m: self.m[key] = []; self.v[key] = []
        self.m[key].append(timestamp)
        self.v[key].append(value)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.m: return ""
        b = bisect_right(self.m[key], timestamp)
        if b == 0: return ""
        return self.v[key][b-1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)