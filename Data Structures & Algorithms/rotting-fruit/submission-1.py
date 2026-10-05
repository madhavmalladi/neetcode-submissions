class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # first count the number of fresh fruit
        # run bfs from the rotten fruit
        # at the end check if all fresh fruit have become rotten
        # (do this by checking if fresh_fruit = 0 at the end)

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        n_rows, n_cols = len(grid), len(grid[0])
        fresh_fruit = 0

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_fruit += 1

        time = 0
        while queue and fresh_fruit > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if new_row < 0 or new_row >= n_rows:
                        continue
                    if new_col < 0 or new_col >= n_cols:
                        continue
                    if grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh_fruit -= 1
                        queue.append((new_row, new_col))
            time += 1

        if fresh_fruit != 0:
            return -1
        else:
            return time
            