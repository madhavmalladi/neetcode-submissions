class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if (nums[0] == target):
            return 0
        if (nums[-1] == target):
            return (len(nums) - 1)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                r = mid - 1
            else:
                l = mid + 1
        return -1