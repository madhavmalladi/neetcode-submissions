class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        charS = list(s)
        charT = list(t)
        charS.sort()
        charT.sort()
        for i in range(len(s)):
            if (charS[i] != charT[i]):
                return False
        return True
            