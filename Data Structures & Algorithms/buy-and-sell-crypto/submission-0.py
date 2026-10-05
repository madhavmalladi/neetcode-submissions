class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        ptr1, ptr2 = 0, 1
        while ptr1 < len(prices):
            ptr2 = ptr1 + 1
            while (ptr2 < len(prices)):
                if (prices[ptr2] - prices[ptr1] > profitMax):
                    profitMax = prices[ptr2] - prices[ptr1]
                ptr2 = ptr2 + 1
            ptr1 = ptr1 + 1
            
        return profitMax