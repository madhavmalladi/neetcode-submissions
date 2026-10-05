class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        nums = [1,2,4,6]
        prefixProduct = [1, 1, 2, 8]
        postfixProduct = [48, 24, 6, 1]
        ans = prefix[i] * postfix[i]
        ans = [48, 24, 12, 8]
        '''

        ans = []
        n = len(nums)
        prefix, postfix = [0 for i in range(n)], [0 for i in range(n)]

        prefix[0] = 1
        postfix[-1] = 1

        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n - 2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]

        for i in range(n):
            ans.append(prefix[i] * postfix[i])

        return ans