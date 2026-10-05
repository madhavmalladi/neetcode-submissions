class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if (self.minimums):
            self.minimums.append(min(val, self.minimums[-1]))
        else:
            self.minimums.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minimums[-1]
