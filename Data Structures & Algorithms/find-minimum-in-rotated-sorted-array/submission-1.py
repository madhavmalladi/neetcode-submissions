class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            # hasn't been rotated, or was rotated n times
            return nums[0]
        min_val = float('inf')

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                min_val = min(min_val, nums[mid])
                l = mid + 1
            else:
                min_val = min(min_val, nums[mid])
                r = mid - 1
        
        return min_val