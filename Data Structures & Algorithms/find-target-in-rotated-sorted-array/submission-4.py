class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[l] <= nums[mid]): # left side is sorted
                if target > nums[mid] or target < nums[l]: # not in between l and mid
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]: # not in between mid and r
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1