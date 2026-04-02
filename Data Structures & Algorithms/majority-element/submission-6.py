class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        votes = 1
        
        for n in nums[1:]:
            votes = votes + 1 if n == majority else votes - 1    
            if votes == 0:
                majority = n
                votes = 1
        
        return majority
