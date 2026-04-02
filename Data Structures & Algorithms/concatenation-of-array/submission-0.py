class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(2):
            for j in range(n):
                ans[n * i + j] = nums[j]
        return ans