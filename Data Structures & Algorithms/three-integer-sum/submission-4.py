class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[j] + nums[k] = 0 - nums[i]
        # [-4, -1, -1, 0, 1, 2] -> [-1, -1, 2] and [-1, 0, 1]
        # for i in range(len(nums))
        #   while nums[i] != nums[i+1]

        ans = []
        nums.sort()

        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            target = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if (nums[l] + nums[r] == target):
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                    r-=1
                elif (nums[l] + nums[r] > target):
                    r -= 1
                else:
                    l += 1


        return ans
                
