class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val - self.min if self.stack else 0)
        self.min = min(self.min, val) if len(self.stack) > 1 else val

    def pop(self) -> None:
        self.min -= min(self.stack.pop(), 0)
        
    def top(self) -> int:
        return max(self.min, self.stack[-1] + self.min)

    def getMin(self) -> int:
        return self.min
