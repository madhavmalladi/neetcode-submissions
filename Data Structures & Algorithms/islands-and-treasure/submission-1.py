from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find a treasure chest and then run bfs from it
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        queue = deque()
        n_rows, n_cols = len(grid), len(grid[0])

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row >= n_rows:
                    continue
                if new_col < 0 or new_col >= n_cols:
                    continue
                if grid[new_row][new_col] == 2147483647:
                    grid[new_row][new_col] = 1 + grid[row][col]
                    queue.append((new_row, new_col))
        
        return None
            