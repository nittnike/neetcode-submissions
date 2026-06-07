class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_prices = prices[0]
        for i in prices:
            min_prices = min(min_prices, i)
            max_profit = max(max_profit, i - min_prices)

        return max_profit