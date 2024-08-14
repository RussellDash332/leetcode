class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    def __repr__(self):
        return str((self.prev.val if self.prev else None, self.val, self.next.val if self.next else None))

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}
        self.head = self.tail = None


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache: return -1
        # remove node
        node = self.cache[key]
        if node.prev and node.next: node.prev.next, node.next.prev = node.next, node.prev
        elif node.prev: node.prev.next = None; self.tail = node.prev # not head
        elif node.next: node.next.prev = None; self.head = node.next # not tail
        else: self.head = self.tail = None
        node.prev = node.next = None
        # reinsert to tail
        if not self.head: self.head = self.tail = node
        else: self.tail.next = node; node.prev = self.tail; self.tail = node
        return node.val[1]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            # remove node
            if node.prev and node.next: node.prev.next, node.next.prev = node.next, node.prev
            elif node.prev: node.prev.next = None; self.tail = node.prev
            elif node.next: node.next.prev = None; self.head = node.next
            else: self.head = self.tail = None
        node = Node((key, value))
        self.cache[key] = node
        # insert node to tail
        if not self.head: self.head = self.tail = node
        else: self.tail.next = node; node.prev = self.tail; self.tail = node
        # if capacity hit, remove head
        if len(self.cache) > self.cap:
            node = self.head
            del self.cache[node.val[0]]
            if node.prev and node.next: node.prev.next, node.next.prev = node.next, node.prev
            elif node.prev: node.prev.next = None; self.tail = node.prev
            elif node.next: node.next.prev = None; self.head = node.next
            else: self.head = self.tail = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)