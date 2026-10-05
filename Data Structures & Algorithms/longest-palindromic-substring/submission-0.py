class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        maxLength = 0

        for i in range(len(s)):

            # palindromes of odd length
            l, r = i, i
            while (l >=0 and r < len(s) and s[r]==s[l]):
                if (r-l+1) > maxLength:
                    maxLength = r-l+1
                    ans = s[l:r+1]
                l -= 1
                r += 1
            
            # palindromes of even length
            l, r = i, i + 1
            while (l >=0 and r < len(s) and s[r]==s[l]):
                if (r-l+1) > maxLength:
                    maxLength = r-l+1
                    ans = s[l:r+1]
                l -= 1
                r += 1
        
        return ans