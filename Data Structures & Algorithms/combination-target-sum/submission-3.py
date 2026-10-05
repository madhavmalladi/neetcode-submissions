class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        subset = []
        curr_sum = 0
        def dfs(i, curr_sum):
            if i >= len(nums):
                return
            if curr_sum > target:
                return
            
            # include it
            subset.append(nums[i])
            curr_sum += nums[i]
            if curr_sum == target:
                ans.append(subset.copy())
            dfs(i, curr_sum) # we can re-use the number
            
            # don't include it
            subset.pop()
            curr_sum -= nums[i]
            dfs(i+1, curr_sum)
        
        dfs(0, 0)
        return ans