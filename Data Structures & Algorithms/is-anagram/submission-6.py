class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        The count of every chracter in 't' should match the count of 
        every character in 's'
        '''

        countS = {}
        for char in s:
            countS[char] = countS.get(char, 0) + 1
        
        for char in t:
            if char not in countS or countS[char] == 0:
                return False
            countS[char] -= 1
        
        for char in countS:
            if (countS[char] != 0):
                return False
        
        return True