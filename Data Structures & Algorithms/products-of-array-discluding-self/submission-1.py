class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        postfix = 1
        result = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            result[i] = prefix[i] * postfix
            postfix *= nums[i]

        return result