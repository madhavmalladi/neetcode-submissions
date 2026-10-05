class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1] * len(nums)
        postfixProduct = [1] * len(nums)

        prefixProduct[0] = 1
        postfixProduct[-1] = 1

        # prefix product loop
        for i in range(1, len(nums)):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]
        
        # postfix product loop
        for i in range(len(nums) - 2, -1, -1):
            postfixProduct[i] = postfixProduct[i+1] * nums[i+1]

        ans = []
        for i in range(len(nums)):
            ans.append(prefixProduct[i] * postfixProduct[i])

        return ans
