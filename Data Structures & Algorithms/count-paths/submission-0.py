class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # [0    1   1
        #. 1    2   3]

        grid = [[0 for i in range(n)] for j in range(m)]

        # we can only enter a square from above or from the left
        
        grid[0][0] = 1

        for row in range(m):
            for col in range(n):
                # adding the cell above
                if (row - 1) >= 0:
                    grid[row][col] += grid[row-1][col]
                
                # adding the cell to the left
                if (col - 1) >= 0:
                    grid[row][col] += grid[row][col-1]
        
        return grid[m-1][n-1]
