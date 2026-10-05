class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10, 5, 9, 11, 2, 5]
        maxProfit = 0 # would be attained if we make no transactions
        left_ptr = 0

        for right_ptr in range(1, len(prices)):
            if prices[right_ptr] > prices[left_ptr]:
                profit = prices[right_ptr] - prices[left_ptr]
                maxProfit = max(maxProfit, profit)
            else:
                left_ptr = right_ptr
        
        return maxProfit
