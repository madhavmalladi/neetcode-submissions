import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min(k) = 1, max(k) = max(piles)
        #   - there is some rate (k) between [1,max(piles)] that is optimal
        # we know the upper and lower bounds, so we could run a binary search 
        # run binary search
            # if total_time with k = mid is less than or equal to h:
                # we can go slower, so move the right pointer
            # if total_time with k = mid is greater than h:
                # we need to move faster, so move the left pointer
        minRate = float('inf')
        l, r = 1, max(piles)

        while l <= r:
            mid = (l+r) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/mid)
            if (total_time <= h): # could be optimal, check for slower rates
                minRate = min(minRate, mid)
                r = mid - 1
            else: # takes too much time, so check for faster rates
                l = mid + 1
        
        return minRate
