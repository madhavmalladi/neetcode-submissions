class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                flattened.append(matrix[i][j])

        # binary search
        l, r = 0, len(flattened) - 1

        while l <= r:
            mid = (l + r) // 2
            if flattened[mid] == target:
                return True
            elif flattened[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False