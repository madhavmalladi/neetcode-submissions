class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = float('inf')

        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            hrs_needed = 0
            for pile in piles:
                hrs_needed += math.ceil(pile/mid)
            
            if hrs_needed <= h:
                min_rate = min(min_rate, mid)
                r = mid - 1
            elif hrs_needed > h:
                l = mid + 1
        
        return min_rate