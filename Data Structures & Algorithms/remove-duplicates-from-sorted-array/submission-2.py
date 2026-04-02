class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        
        for right in range(1, len(nums)):
            nums[left] = nums[right]
            if nums[left] != nums[left - 1]:
                left += 1

        return left