class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0, 0, 0]
        for num in nums:
            arr[num] += 1
        
        for i in range(len(nums)):
            if (i < arr[0]):
                nums[i] = 0
            elif (i >= arr[0] and i <(arr[0] + arr[1])):
                nums[i] = 1
            else:
                nums[i] = 2
    