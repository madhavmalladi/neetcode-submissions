class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0,3,2,5,4,6,1,1]
        maxSequence = 0
        numSet = set(nums)

        for num in nums:
            currLen = 1
            if (num-1) in numSet:
                continue
            while (num + 1) in numSet:
                currLen += 1
                num += 1
            
            maxSequence = max(maxSequence, currLen)

        return maxSequence
            