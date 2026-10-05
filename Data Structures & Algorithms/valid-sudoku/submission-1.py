class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # (row//3, col//3) is the key

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == ".":
                    continue
                if val in rows[row]:
                    return False
                elif val in cols[col]:
                    return False
                elif val in squares[(row//3, col//3)]: 
                    return False

                rows[row].add(val)
                cols[col].add(val)
                squares[(row//3, col//3)].add(val)

        return True