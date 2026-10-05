from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n_rows = len(grid)
        n_cols = len(grid[0])
        queue = deque()
        
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 0: # treasure chest
                    queue.append((r, c))

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                # check bounds and if neighbor is unvisited land
                if (0 <= new_r < n_rows and 0 <= new_c < n_cols and 
                grid[new_r][new_c] == 2147483647):
                    grid[new_r][new_c] = grid[r][c] + 1
                    # add newly updated land cell to queue
                    queue.append((new_r, new_c))
        
        return None





