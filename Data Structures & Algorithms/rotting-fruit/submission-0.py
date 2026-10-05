from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        queue = deque()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        fresh_fruit = 0

        # add all rotten fruits to the queue
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_fruit += 1
        
        time = 0
        while queue and fresh_fruit > 0:
            # process level by level so we can count time
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc

                    if (0 <= new_r < n_rows and
                        0 <= new_c < n_cols and
                        grid[new_r][new_c] == 1):
                        # make this fruit rotten
                        grid[new_r][new_c] = 2
                        fresh_fruit -= 1
                        queue.append((new_r, new_c))
                
            time += 1

        if fresh_fruit != 0:
            return -1
        
        return time


