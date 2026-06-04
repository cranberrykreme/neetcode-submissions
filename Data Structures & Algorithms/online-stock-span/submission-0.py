class StockSpanner:

    def __init__(self):
        self.values = []
        self.spans = []

    def next(self, price: int) -> int:
        loc = len(self.spans)-1
        days = 1
        while loc >= 0 and self.values[loc] <= price:
            days += self.spans[loc]
            self.values.pop()
            self.spans.pop()
            loc -= 1
        self.values.append(price)
        self.spans.append(days)
        return days





# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)