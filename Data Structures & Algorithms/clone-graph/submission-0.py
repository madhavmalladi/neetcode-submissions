"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            oldToNew[node] = Node(node.val)
            copy = oldToNew[node]
            for adj in node.neighbors:
                copy.neighbors.append(dfs(adj))
            return copy

        if node:
            return dfs(node)
        else:
            None

        