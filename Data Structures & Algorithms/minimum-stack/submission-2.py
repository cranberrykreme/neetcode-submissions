class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.ordered_stack[-1] if self.ordered_stack else val)
        self.ordered_stack.append(val)

    def pop(self) -> None:
        del self.stack[-1]
        del self.ordered_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ordered_stack[-1]
