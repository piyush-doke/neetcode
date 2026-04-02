class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = 0

        for i in range(len(nums)):
            if majority_count == 0:
                majority = nums[i]
            if nums[i] == majority:
                majority_count += 1
            else:
                majority_count -= 1
        
        return majority