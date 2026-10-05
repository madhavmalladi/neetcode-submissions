"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None} # mapping every old node to the copy we create

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldToCopy[curr]
            if curr.next is None:
                copy.next = None
            else:
                copy.next = oldToCopy[curr.next]
            
            if curr.random is None:
                copy.random = None
            else:
                copy.random = oldToCopy[curr.random]
            
            curr = curr.next

        return oldToCopy[head]