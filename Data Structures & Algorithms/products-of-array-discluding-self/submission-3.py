class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = [0] * len(nums)
        prefix = [0] * len(nums)
        output = [0] * len(nums)

        # calculate prefix products
        prefix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        # calculate the postfix products
        postfix[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        # calculate the output
        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i]

        return output