class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 = 0, 0
        for c in cost:
            curr = c + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)
