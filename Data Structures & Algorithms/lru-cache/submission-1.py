class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove_node(self, node: Node):
        prevN = node.prev
        nextN = node.next

        prevN.next = nextN
        nextN.prev = prevN
    
    def insert_node(self, node: Node):
        temp = self.right.prev
        self.right.prev = node
        temp.next = node
        node.next = self.right
        node.prev = temp

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else: # we need to make this the MRU
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove_node(lru)
            del self.cache[lru.key]

        
