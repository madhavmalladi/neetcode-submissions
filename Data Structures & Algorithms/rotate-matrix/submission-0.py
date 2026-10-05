class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the top left value
                topLeft = matrix[top][l + i]

                # move the bottom left value into the top left
                matrix[top][l + i] = matrix[bottom - i][l] # bottom moves up a row (row-1)

                # move the bottom right value into the bottom left
                matrix[bottom - i][l] = matrix[bottom][r-i]

                # move the top right value into the bottom right
                matrix[bottom][r-i] = matrix[top + i][r]

                # move the top left value into the top right
                matrix[top + i][r] = topLeft
        
            l += 1
            r -=1