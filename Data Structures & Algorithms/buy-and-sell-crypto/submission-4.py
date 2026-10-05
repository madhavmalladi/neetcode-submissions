class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        ptr1 = 0

        for ptr2 in range(1, len(prices)):
            profit = prices[ptr2] - prices[ptr1]
            if prices[ptr2] < prices[ptr1]:
                ptr1 = ptr2
            maxP = max(maxP, profit)

        return maxP