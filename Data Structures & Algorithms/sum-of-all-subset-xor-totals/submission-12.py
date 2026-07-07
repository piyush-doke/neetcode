class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(start, xor):
            nonlocal total
            for i in range(start, len(nums)):
                subset_xor = xor ^ nums[i]
                backtrack(i + 1, subset_xor)
                total += subset_xor

        total = 0
        backtrack(0, 0)
        return total