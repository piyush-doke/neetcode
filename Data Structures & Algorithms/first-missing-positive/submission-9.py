class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            n = nums[i]
            if n > 0 and n < len(nums) and n != nums[n - 1]:
                temp = nums[n - 1]
                nums[n - 1] = n
                nums[i] = temp
            else:
                i += 1

        for i, n in enumerate(nums):
            if i + 1 != n:
                return i + 1
        
        return len(nums) + 1