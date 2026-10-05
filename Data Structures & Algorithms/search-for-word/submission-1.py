class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def backtrack(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= len(board):
                return False
            if col < 0 or col >= len(board[0]):
                return False 
            if word[index] != board[row][col]:
                return False
            if (row, col) in path:
                return False

            path.add((row, col))

            up = backtrack(row-1, col, index + 1)
            down = backtrack(row + 1, col, index + 1)
            left = backtrack(row, col - 1, index + 1)
            right = backtrack(row, col + 1, index + 1)

            ans = up or down or right or left
            path.remove((row, col))
            return ans

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
        
        return False
