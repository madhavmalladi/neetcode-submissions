class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        candidates.sort()

        def dfs(start, remaining):
            if remaining == 0:
                ans.append(subset.copy())
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                subset.append(candidates[i])
                dfs(i + 1, remaining - candidates[i])
                subset.pop()
        
        dfs(0, target)
        return ans

            


