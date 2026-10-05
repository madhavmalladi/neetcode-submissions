class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        n_rows, n_cols = len(grid), len(grid[0])
        curr_area = 0

        def dfs(row, col):
            nonlocal curr_area

            if row < 0 or row >= n_rows:
                return
            if col < 0 or col >= n_cols:
                return
            if grid[row][col] == 0:
                return
            
            grid[row][col] = 0
            curr_area += 1
            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        max_area = 0
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1:
                    curr_area = 0
                    dfs(row, col)
                    max_area = max(max_area, curr_area)
        
        return max_area
        

