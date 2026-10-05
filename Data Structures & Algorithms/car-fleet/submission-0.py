class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)): 
            arr.append([position[i], speed[i]])
        arr = sorted(arr)

        stack = []
        for pos, speed in arr[::-1]:
            stack.append((target - pos) / speed)
            if (len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
        
        return len(stack)