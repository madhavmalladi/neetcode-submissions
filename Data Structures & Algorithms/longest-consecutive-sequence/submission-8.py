class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set()

        for num in nums:
            numSet.add(num)

        for num in nums:
            currLen = 1

            if (num-1) in numSet:
                continue

            while (num + 1) in numSet:
                currLen += 1
                num += 1
                
            maxLen = max(maxLen, currLen)

        return maxLen