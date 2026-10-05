class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0 for i in range(len(height))]
        maxRight = [0 for i in range(len(height))]
        totalTrapped = 0

        maxLeft[0] = 0
        maxRight[-1] = 0

        # calculating the maxLeft
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        
        # calculating the maxRight
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])

        for i in range(len(height)):
            diff = min(maxLeft[i], maxRight[i]) - height[i]
            if diff > 0:
                totalTrapped += diff
        
        return totalTrapped