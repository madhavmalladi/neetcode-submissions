class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        string = []

        def backtrack(opened, closed):
            if len(string) == (n * 2):
                ans.append(''.join(string))
                return
            
            # if opened == closed, we can only open a parentheses
            if opened == closed:
                string.append('(')
                backtrack(opened + 1, closed)
                string.pop()
            
            # opened != closed and we can open another pair
            elif opened < n:
                # open a new pair
                string.append('(')
                backtrack(opened + 1, closed)
                string.pop()

                # close an existing pair
                string.append(')')
                backtrack(opened, closed + 1)
                string.pop()
            # we are forced to close
            else:
                string.append(')')
                backtrack(opened, closed + 1)
                string.pop()
        
        backtrack(0,0)
        return ans
                
            
