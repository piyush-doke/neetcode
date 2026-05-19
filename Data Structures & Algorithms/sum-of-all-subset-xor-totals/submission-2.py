class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(xor, i):
            if i == len(nums): return xor
            return dfs(xor ^ nums[i], i + 1) + dfs(xor, i + 1)
        return dfs(0, 0)