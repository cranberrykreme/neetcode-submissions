class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        curr_highest, buy_price = prices[0], prices[0]
        profit = 0
        for i in range(1, n):
            price = prices[i]
            if price > curr_highest:
                curr_highest = price
            if price < prices[i-1] or i == (n-1):
                profit += curr_highest - buy_price
                curr_highest, buy_price = price, price
        return profit

