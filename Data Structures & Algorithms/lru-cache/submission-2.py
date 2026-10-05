class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}              # key -> Node
        self.capacity = capacity

        self.left = Node(0, 0)       # LRU dummy
        self.right = Node(0, 0)      # MRU dummy

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert a node at the MRU end (right side)
    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to MRU position
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.remove(node)
            self.insert(node)

        # New key
        else:
            if len(self.cache) == self.capacity:
                # Remove LRU node
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]

            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node