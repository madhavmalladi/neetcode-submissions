class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = {num : count}
        # freq = [[]] * len(nums)
        # counts = {1:1, 2:5, 3:4, 4:4}
        # freq[1] = [1], freq[5] = [2], freq[4] = [3,4]

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]

        for num in counts:
            count = counts[num]
            freq[count].append(num)

        ans = []
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                if len(ans) < k:
                    ans.append(num)
                else:
                    return ans

        return ans
