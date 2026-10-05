class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node, adj in edges:
            graph[node].append(adj)
            graph[adj].append(node)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for adj in graph[node]:
                dfs(adj)

            return
        
        num_components = 0
        for i in range(n):
            if i in visited:
                continue
            num_components += 1
            dfs(i)

        return num_components
        