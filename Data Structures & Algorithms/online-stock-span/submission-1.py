class StockSpanner:

    def __init__(self):
        self.values = []

    def next(self, price: int) -> int:
        days = 1
        while self.values and self.values[-1][0] <= price:
            days += self.values.pop()[1]
        self.values.append((price,days))
        return days





# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)