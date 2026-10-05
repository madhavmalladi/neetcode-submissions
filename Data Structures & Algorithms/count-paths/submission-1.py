class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # [0    1   1
        #. 1    2   3]

        grid = [[1 for i in range(n)] for j in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                # we can only enter a square from above or from the left
                grid[row][col] = grid[row-1][col] + grid[row][col-1]
        return grid[m-1][n-1]
