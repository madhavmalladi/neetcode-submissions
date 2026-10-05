class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # (r//3, c//3)
        rows = defaultdict(set)
        cols = defaultdict(set)
        three_by_three = defaultdict(set)

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.':
                    continue
                if value in rows[row]:
                    return False
                if value in cols[col]:
                    return False
                if value in three_by_three[(row//3, col//3)]:
                    return False
                
                rows[row].add(value)
                cols[col].add(value)
                three_by_three[(row//3, col//3)].add(value)
        
        return True
