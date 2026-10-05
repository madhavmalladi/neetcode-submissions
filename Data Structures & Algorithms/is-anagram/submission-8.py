class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        for c in s:
            countS[c] = countS.get(c, 0) + 1
        
        for c in t:
            if c not in countS:
                return False
            
            if countS[c] == 0:
                return False
            
            countS[c] -= 1

        for char in s:
            if countS[char] != 0:
                return False
        
        return True