class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = nums[-1]
        goalIndex = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if (goalIndex - i <= nums[i]):
                goal = nums[i]
                goalIndex = i
            else:
                continue
        
        return (goalIndex == 0)
