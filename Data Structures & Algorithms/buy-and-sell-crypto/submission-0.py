class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest, profit = prices[0], 0
        for p in prices[1:]:
            profit = max(profit, p - smallest)
            smallest = min(smallest, p)
        return profit
