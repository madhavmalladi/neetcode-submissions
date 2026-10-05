class MinStack:
    # stack = [1, 2, 0]
    # minimum_vals = [1, 1, 0]

    def __init__(self):
        self.stack = []
        self.minimum_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # comparing val to minimum_vals[-1]
        if (self.minimum_vals):
            self.minimum_vals.append(min(val, self.minimum_vals[-1]))
        else:
            self.minimum_vals.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_vals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_vals[-1]
