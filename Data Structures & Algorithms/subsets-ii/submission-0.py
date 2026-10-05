class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        nums.sort()

        def dfs(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return
            
            # include it
            subset.append(nums[i])
            dfs(i+1)

            # don't include it
            subset.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            dfs(i)

        dfs(0)
        return ans