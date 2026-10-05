class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                prev_index, prev_height = stack.pop()
                maxArea = max((index - prev_index) * prev_height, maxArea)
                start = prev_index
            stack.append((start, height))
        
        while stack:
            prev_index, prev_height = stack.pop()
            maxArea = max((n - prev_index) * prev_height, maxArea)
        
        return maxArea

