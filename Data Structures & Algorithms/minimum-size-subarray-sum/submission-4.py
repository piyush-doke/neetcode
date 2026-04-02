class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = window_sum = 0
        window_length = float("inf")

        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                window_length = min(window_length, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        return 0 if window_length == float("inf") else window_length
