class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        permutation = []
        used = set()

        def dfs():
            if len(permutation) == len(nums):
                ans.append(permutation.copy())
                return

            for i in range(len(nums)):
                if i in used:
                    continue
                
                used.add(i)
                permutation.append(nums[i])

                dfs()

                # backtrack
                used.remove(i)
                permutation.pop()
        
        dfs()
        return ans

            

        