class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # maps key to nodes
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    # insert to the right
    def insert(self, node):
        temp = self.right.prev
        self.right.prev, temp.next = node, node
        node.next, node.prev = self.right, temp
    def get(self, key: int) -> int:
        if key in self.cache:
            # we need to make this key the MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
