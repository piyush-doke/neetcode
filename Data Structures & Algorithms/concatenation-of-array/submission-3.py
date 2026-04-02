class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums) * 2
        for i, n in enumerate(nums):
            result[i] = result[len(nums) + i] = n
        return result