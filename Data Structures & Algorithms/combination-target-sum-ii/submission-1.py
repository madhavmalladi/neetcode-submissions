class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        subset = []
        curr_sum = 0
        def dfs(i, curr_sum):
            if i >= len(candidates):
                return
            if curr_sum >= target:
                return

            # include it
            subset.append(candidates[i])
            curr_sum += candidates[i]
            if curr_sum == target:
                ans.append(subset.copy())
            dfs(i+1, curr_sum)

            # don't include it
            subset.pop()
            curr_sum -= candidates[i]
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, curr_sum)

        dfs(0, curr_sum)
        return ans