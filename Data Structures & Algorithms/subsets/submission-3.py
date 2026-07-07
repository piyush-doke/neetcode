class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            for i in range(start, len(nums)):
                subset.append(nums[i])
                result.append(subset[:])
                backtrack(i + 1, subset)
                subset.pop()
        
        result = [[]]
        backtrack(0, [])
        return result