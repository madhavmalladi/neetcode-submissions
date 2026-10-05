class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        ptr1, ptr2 = 0, 1
        while ptr2 < len(prices):
            if (prices[ptr1] < prices[ptr2]):
                profit = prices[ptr2] - prices[ptr1]
                profitMax = max(profitMax, profit)
            else:
                ptr1 = ptr2
            ptr2 += 1
        return profitMax