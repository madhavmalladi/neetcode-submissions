class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)] # each node begins as its own parent (1-indexed)
        rank = [1] * (len(edges) + 1)

        def find(node):
            if node == parent[node]:
                return parent[node]
            parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return False
            
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]