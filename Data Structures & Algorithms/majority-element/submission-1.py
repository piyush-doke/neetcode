class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        majority_count = 0
        for i in range(len(nums)):
            if nums[i] == majority:
                majority_count += 1
            else:
                majority_count -= 1
            
            if majority_count < 0:
                majority = nums[i]
        
        return majority