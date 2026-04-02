class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost, max_profit = float("inf"), 0
        for p in prices:
            max_profit = max(max_profit, p - min_cost)
            min_cost = min(min_cost, p)
        return max_profit