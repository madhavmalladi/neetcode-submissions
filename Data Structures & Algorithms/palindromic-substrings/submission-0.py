class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        for i in range(len(s)):
            
            # palindromes of odd length
            l = r = i
            while (l >= 0 and r < len(s) and s[r] == s[l]):
                ans += 1
                l -= 1
                r += 1
            
            # palindromes of even length
            l, r = i, i+1
            while (l >=0 and r < len(s) and s[r] == s[l]):
                ans += 1
                l -= 1
                r += 1
        
        return ans