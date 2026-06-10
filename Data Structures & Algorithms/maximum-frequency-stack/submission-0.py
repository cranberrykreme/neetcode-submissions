class FreqStack:

    def __init__(self):
        self.stack = [[]]
        self.counts = {}

    def push(self, val: int) -> None:
        cnt = self.counts.get(val,0)+1
        self.counts[val] = cnt
        if cnt == len(self.stack):
            self.stack.append([])
        self.stack[cnt].append(val)

    def pop(self) -> int:
        freq_val = self.stack[-1].pop()
        self.counts[freq_val] -= 1
        if not self.stack[-1]:
            self.stack.pop()
        return freq_val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()