class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hold a var called max_length
        # have a array of length 26, to hold the frequencies of each chracter in the current window
        # use a sliding window approach
            # if the cost, which is the (size of the window) - (max frequency in the window) is
                # <=k, then continue moving the right pointer
                # > k, then move the left pointer
        
        # return max_length at the end

        max_length = 1
        frequencies = [0] * 26

        left = 0
        for right in range(len(s)):
            frequencies[ord(s[right]) - ord('A')] += 1

            while (right - left + 1) - max(frequencies) > k: # cost > k, so move left ptr
                frequencies[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length
