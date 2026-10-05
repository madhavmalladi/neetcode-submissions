class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSequence = 0
        
        for num in nums:
            curr_sequence = 1
            i = 1
            while (num + i) in nums:
                curr_sequence += 1
                i += 1
            maxSequence = max(maxSequence, curr_sequence)
        
        return maxSequence