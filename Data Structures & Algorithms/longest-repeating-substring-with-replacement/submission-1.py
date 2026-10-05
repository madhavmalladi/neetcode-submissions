class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 1
        frequencies = [0] * 26

        left = 0
        for right in range(len(s)):
            frequencies[ord(s[right]) - ord('A')] += 1

            while (right - left + 1) - max(frequencies) > k:
                frequencies[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
            
