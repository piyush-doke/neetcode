class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        profit = 0
        for curr in prices[1:]:
            profit += max(curr - prev, 0)
            prev = curr
        return profit