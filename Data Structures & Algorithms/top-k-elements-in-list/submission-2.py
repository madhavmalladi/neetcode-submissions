class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        frequencies = [[] for i in range(len(nums) + 1)]
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        
        for num, count in countMap.items():
            frequencies[count].append(num)
        
        ans = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                ans.append(num)
                if (len(ans) == k):
                    return ans
        
        return ans
