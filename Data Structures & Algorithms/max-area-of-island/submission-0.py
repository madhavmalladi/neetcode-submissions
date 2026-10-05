class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        curr_area = 0
        max_area = 0

        def dfs(row, col):
            nonlocal curr_area

            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == 0:
                return
            else:
                curr_area += 1 

            grid[row][col] = 0

            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    curr_area = 0
                    dfs(row, col)
                    max_area = max(max_area, curr_area)
        
        return max_area

