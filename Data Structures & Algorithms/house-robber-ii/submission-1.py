class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev1, prev2 = 0, 0

        for n in nums[1:]:
            cur = max(prev1, prev2 + n)
            prev2 = prev1
            prev1 = cur
        
        tmp = prev1
        prev1, prev2 = 0, 0
        for n in nums[:-1]:
            cur = max(prev1, prev2 + n)
            prev2 = prev1
            prev1 = cur
        
        return max(tmp, prev1)