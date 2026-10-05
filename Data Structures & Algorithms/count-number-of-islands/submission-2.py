class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n_rows, n_cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(row, col):
            if row < 0 or row >= n_rows:
                return
            if col < 0 or col >= n_cols:
                return
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == "0":
                    continue
                num_islands += 1
                dfs(row, col)

        return num_islands