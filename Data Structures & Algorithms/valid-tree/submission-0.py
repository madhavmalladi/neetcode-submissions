class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for node, adj in edges:
            graph[node].append(adj)
            graph[adj].append(node)
        
        visiting = set()

        def dfs(node, prev):
            if node in visiting: # there is a cycle
                return False

            visiting.add(node)

            for adj in graph[node]:
                if adj != prev:
                    if not dfs(adj, node):
                        return False
            
            return True

        if not dfs(0, -1):
            return False
        
        if len(visiting) == n:
            return True
        else:
            return False