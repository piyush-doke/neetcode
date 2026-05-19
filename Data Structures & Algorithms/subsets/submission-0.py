class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            result += [r + [n] for r in result]
        return result
