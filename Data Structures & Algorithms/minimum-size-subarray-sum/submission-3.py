class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = window_sum = 0
        window_length = float("inf")

        while right < len(nums):
            if window_sum < target:
                window_sum += nums[right]
                right += 1
            else:
                window_length = min(window_length, right - left)
                window_sum -= nums[left]
                left += 1
        
        while window_sum >= target:
            window_length = min(window_length, right - left)
            window_sum -= nums[left]
            left += 1
        
        return 0 if window_length == float("inf") else window_length
