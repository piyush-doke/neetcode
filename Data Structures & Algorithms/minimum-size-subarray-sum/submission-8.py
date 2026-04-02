class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = window_sum = 0
        min_length = float('inf')

        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum >= target:
                min_length = min(min_length, r - l + 1)
                window_sum -= nums[l]
                l += 1

        return 0 if min_length == float('inf') else min_length