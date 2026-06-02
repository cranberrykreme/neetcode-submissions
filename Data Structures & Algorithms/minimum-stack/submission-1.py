class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        prev_low = float('inf')
        if self.ordered_stack:
            prev_low = self.ordered_stack[-1]
        self.ordered_stack.append(min(val, prev_low))

    def pop(self) -> None:
        del self.stack[-1]
        del self.ordered_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ordered_stack[-1]
