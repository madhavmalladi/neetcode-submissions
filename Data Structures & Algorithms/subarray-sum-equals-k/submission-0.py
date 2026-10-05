class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curr_sum = 0
        prefixSums = {0:1}
        
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            ans += prefixSums.get(diff, 0)
            prefixSums[curr_sum] = 1 + prefixSums.get(curr_sum, 0)

        return ans 