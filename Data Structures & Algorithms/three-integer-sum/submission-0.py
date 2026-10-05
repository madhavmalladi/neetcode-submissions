class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n  = len(nums)
        ans = set()
        nums = sorted(nums)

        for i in range(n):
            l, r = i+1, n-1
            target = 0 - nums[i]
            while l < r:
                if (nums[l] + nums[r] == target):
                    triple = sorted([nums[i], nums[l], nums[r]])
                    ans.add(tuple(triple))
                    l += 1
                    r-=1
                elif (nums[l] + nums[r] < target):
                    l += 1
                else:
                    r -= 1
        
        return list(ans)
                
