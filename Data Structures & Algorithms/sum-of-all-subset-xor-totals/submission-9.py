class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, xor):
            if i == len(nums):
                return xor
            return dfs(i + 1, xor ^ nums[i]) + dfs(i + 1, xor)
        return dfs(0, 0)
