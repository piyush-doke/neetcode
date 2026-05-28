class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0

        def backtrack(xor, start):
            nonlocal result
            result += xor
            for i in range(start, len(nums)):
                backtrack(xor ^ nums[i], i + 1)
        
        backtrack(0, 0)
        return result
