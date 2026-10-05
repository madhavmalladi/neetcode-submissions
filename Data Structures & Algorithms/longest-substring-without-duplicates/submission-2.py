class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcdbyxr
        #   'cdb'
        # while char is in our set, keep popping from the left of the sliding window

        substringSet = set()
        longest = 0
        left_ptr = 0

        for right_ptr in range(len(s)):
            char = s[right_ptr]
            while char in substringSet:
                substringSet.remove(s[left_ptr])
                left_ptr += 1
            substringSet.add(char)
            longest = max(longest, right_ptr - left_ptr + 1)

        return longest