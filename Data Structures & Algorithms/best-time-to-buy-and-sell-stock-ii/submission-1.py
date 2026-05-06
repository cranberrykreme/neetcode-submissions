class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            if price > prices[i-1]:
                profit += price - prices[i-1]
        return profit

