class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = window_sum = 0
        min_length = len(nums) + 1

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                min_length = min(min_length, r - l + 1)
                window_sum -= nums[l]
                l += 1
        
        if min_length > len(nums):
            min_length = 0
        
        return min_length