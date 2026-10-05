class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ans = []
        subset = []

        if len(digits) == 0:
            return []

        def backtrack(index_of_string):
            if len(subset) == len(digits):
                ans.append(''.join(subset.copy()))
                return

            options = mapping[digits[index_of_string]]
            for letter in options:
                subset.append(letter)
                backtrack(index_of_string + 1)
                subset.pop()
            
            
        backtrack(0)
        return ans


        