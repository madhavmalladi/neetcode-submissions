class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # (temp, index) pairs

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                ans[stackIndex] = (i - stackIndex)
            stack.append([temperature, i])
        
        return ans

