class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                newStr += char
        newStr = newStr.lower()
        return newStr == newStr[::-1]