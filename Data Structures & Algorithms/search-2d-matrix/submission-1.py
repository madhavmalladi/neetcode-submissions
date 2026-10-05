class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # (m*n) - 1 elements
            # let index = i for each element
                # row = i // n
                # column = (i - 1) % n
        
        # l, r = 0, m*n - 1
            # calculate the row/column for the mid
            # compare the matrix[mid_row, mid_col] to the target
                # based on the result:
                    # if the val is < target, then move l
                    # if val > target, move r
                    # if val == target:
                        # return True
            # if we exit the loop (l > r), then return false

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = mid // n, (mid) % n
            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] < target):
                l = mid + 1
            else:
                r = mid - 1
        
        return False
