class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= len(grid):
                return 0
            if col < 0 or col >= len(grid[0]):
                return 0
            if grid[row][col] == 0:
                return 0
            if (row, col) in visited:
                return 0

            visited.add((row, col))

            return (1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1))
        
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_area = max(max_area, dfs(row, col))
        
        return max_area

