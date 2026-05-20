class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            curr_profit = prices[i] - bought
            if curr_profit > profit:
                profit = curr_profit
            elif curr_profit < 0:
                bought = prices[i]
        return profit