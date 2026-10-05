class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n_rows, n_cols = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= n_rows:
                return
            if col < 0 or col >= n_cols:
                return
            if board[row][col] == "X":
                return
            if board[row][col] == "V":
                return
            
            # V for 'visited'
            board[row][col] = "V"
            for dr, dc in directions:
                dfs(row+dr, col+dc)

        '''
        run dfs from all of the bordering O's. This way, we mark all
        O's that are reachable from borders with a 'V'
        '''
        # left and right borders
        for i in range(n_rows):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][n_cols-1] == "O":
                dfs(i, n_cols-1)
        # top and bottom borders
        for i in range(n_cols):
            if board[0][i] == "O":
                dfs(0, i)
            if board[n_rows-1][i] == "O":
                dfs(n_rows-1, i)
        
        '''
        at this point, all surrounded O's are stil O's, and all unsurrounded
        O's have been changed to 'V'. We can now replace all surrounded O's
        with 'X' and all V's with 'O'
        '''
        for row in range(n_rows):
            for col in range(n_cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "V":
                    board[row][col] = "O"
        
        return None
