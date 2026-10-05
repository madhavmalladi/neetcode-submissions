class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        subset = []
        def dfs(i, curr_sum):
            if i >= len(nums):
                return
            if curr_sum > target:
                return
            
            # decide to add nums[i]
            subset.append(nums[i])
            curr_sum += nums[i]
            if curr_sum == target:
                ans.append(subset.copy())
            dfs(i, curr_sum)

            # decide not to add nums[i]
            subset.pop()
            curr_sum -= nums[i]
            dfs(i+1, curr_sum)
        
        dfs(0, 0)
        return ans