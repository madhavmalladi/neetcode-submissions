class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # for this problem, im thinking of the following approach: have 2 2d lists: caled pacific and atlantic. these will be boolean matrices, representing if each cell can reach the respective ocean. i would then run a loop through veery cell at the end, and if it reachesboth pacific and atlantic, then i would append it to the answr array. to find if a cell should be marked True, i would start with the border rows/cols and mark them as true for the respective ocean. i would then expand to the other cells, and only mark as true if the adjacent cell is higher value.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n_rows, n_cols = len(heights), len(heights[0])
        pacific = [[False for _ in range(n_cols)] for _ in range(n_rows)]
        atlantic = [[False for _ in range(n_cols)] for _ in range(n_rows)]
        pacific_queue = deque()
        atlantic_queue = deque()

        # mark the border rows/cols as True
        # top row for pacific, bottom row for atlantic
        for i in range(n_cols):
            pacific[0][i] = True
            pacific_queue.append((0, i))

            atlantic[n_rows-1][i] = True
            atlantic_queue.append((n_rows-1, i))
        # left col for pacific, right col for atlantic
        for i in range(n_rows):
            pacific[i][0] = True
            pacific_queue.append((i, 0))

            atlantic[i][n_cols-1] = True
            atlantic_queue.append((i, n_cols-1))

        # build the pacific matrix
        while pacific_queue:
            row, col = pacific_queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row >= n_rows:
                    continue
                if new_col < 0 or new_col >= n_cols:
                    continue
                if pacific[new_row][new_col] == True:
                    continue
                
                if heights[new_row][new_col] >= heights[row][col]:
                    pacific[new_row][new_col] = True
                    pacific_queue.append((new_row, new_col))
        
        # build the atlantic matrix
        while atlantic_queue:
            row, col = atlantic_queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row >= n_rows:
                    continue
                if new_col < 0 or new_col >= n_cols:
                    continue
                if atlantic[new_row][new_col] == True:
                    continue
                
                if heights[new_row][new_col] >= heights[row][col]:
                    atlantic[new_row][new_col] = True
                    atlantic_queue.append((new_row, new_col))

        ans = []
        for row in range(n_rows):
            for col in range(n_cols):
                if pacific[row][col] and atlantic[row][col]:
                    ans.append([row, col])
        
        return ans

        
        
