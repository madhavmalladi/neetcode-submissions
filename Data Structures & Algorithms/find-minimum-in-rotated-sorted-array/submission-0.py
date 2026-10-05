class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if the nums[-1] > nums[0], then return nums[0] because the array hasnt been rotated
        #    OR has been rotated n times

        # the pivot, which is where the minimum we are trying to find is next to, is where for some i,
        #     nums[i-1] > nums[i]

        # if nums[mid] > nums[r] then min is between mid and r
        # if nums[mid] < nums[l] then min is between l and mid

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[r]

