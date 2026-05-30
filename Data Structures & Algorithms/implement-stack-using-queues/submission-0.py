class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        var = self.stack[-1]
        del self.stack[-1]
        return var

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) < 1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()