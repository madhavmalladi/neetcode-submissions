class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def backtrack(row, col, index_of_word):
            if index_of_word == len(word):
                return True
                
            if row < 0 or row >= len(board):
                return False
            if col < 0 or col >= len(board[0]):
                return False
            if board[row][col] != word[index_of_word]:
                return False
            if (row, col) in path:
                return False
            
            path.add((row, col))

            up = backtrack(row - 1, col, index_of_word + 1)
            down = backtrack(row + 1, col, index_of_word + 1)
            left = backtrack(row, col - 1, index_of_word + 1)
            right = backtrack(row, col + 1, index_of_word + 1)

            path.remove((row, col))
            return up or down or left or right

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r,c,0):
                    return True

        return False        
            
            