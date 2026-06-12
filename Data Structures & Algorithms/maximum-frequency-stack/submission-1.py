class FreqStack:

    def __init__(self):
        self.stack = [[]]
        self.counts = {}

    def push(self, val: int) -> None:
        curr_count = self.counts.get(val, 0) + 1
        self.counts[val] = curr_count
        if curr_count == len(self.stack):
            self.stack.append([])
        self.stack[curr_count].append(val)

    def pop(self) -> int:
        max_val = self.stack[-1].pop()
        self.counts[max_val] -= 1
        if not self.stack[-1]:
            self.stack.pop()
        return max_val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()