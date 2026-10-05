class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = []

        for i in range(n):
            if ( i > 0 and nums[i] == nums[i-1]):
                continue
            l, r = i+1, n-1
            
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                
                if (curr_sum == 0):
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                    r -=1
                
                elif (curr_sum < 0):
                    l += 1
                else:
                    r -= 1
        
        return ans
                    

            