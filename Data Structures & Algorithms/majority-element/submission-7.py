class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        
        for n in nums:
            if votes == 0:
                majority = n
            votes += 1 if n == majority else -1
        
        return majority
