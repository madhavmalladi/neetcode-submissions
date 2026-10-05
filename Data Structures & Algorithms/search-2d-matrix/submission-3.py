class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # finding the optimal row
        l, r = 0, rows - 1
        optimal_row = 0
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target or matrix[mid][cols-1] == target:
                return True
            elif matrix[mid][0] < target < matrix[mid][cols-1]:
                optimal_row = mid
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[optimal_row][mid] == target:
                return True
            elif matrix[optimal_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False