class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter
        '''
        counts = {1:1, 2:3, 3:2, 4:2}
        frequencies = [0] * n
        frequencies[i] = [] that stores the elements in nums w/ count i
        for each value in counts:
            frequencies[3] should contain 2
            frequencies[2] should contain [3,4]
        '''

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        frequencies = [[] for i in range(len(nums) + 1)]
        for num in counts:
            count = counts[num]
            frequencies[count].append(num) #freq[3] = [2], freq[2] = [3,4]

        ans = []
        for i in range(len(frequencies) - 1, -1, -1):
            for num in frequencies[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        return ans

