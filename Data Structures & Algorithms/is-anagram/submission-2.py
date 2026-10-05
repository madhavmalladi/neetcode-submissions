class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        countS = {}
        for char in s:
            countS[char] = countS.get(char,0) + 1
        for char in t:
            if ((char not in countS) or (countS[char] == 0)):
                return False
            countS[char] = countS[char] - 1
        return True