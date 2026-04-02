class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]

        for n in nums:
            cur = max(prev1, prev2 + n)
            prev2 = prev1
            prev1 = cur

        return prev1
