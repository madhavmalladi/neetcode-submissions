class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        num_rows, num_cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(row, col):
            if row < 0 or row >= num_rows:
                return
            if col < 0 or col >= num_cols:
                return
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    num_islands += 1
        
        return num_islands


