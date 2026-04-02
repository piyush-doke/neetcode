class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = [1] * len(nums)
        for i in range(1, len(nums)):
            preProd[i] = nums[i - 1] * preProd[i - 1]
        
        postProd = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            postProd[i] = nums[i + 1] * postProd[i + 1]
        
        return [preProd[i] * postProd[i] for i in range(len(nums))]
        