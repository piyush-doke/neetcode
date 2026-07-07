class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, total, curr):
            if total == target:
                result.append(curr[:])
            elif total < target:
                for i in range(start, len(nums)):
                    curr.append(nums[i])
                    backtrack(i, total + nums[i], curr)
                    curr.pop()

        result = []
        backtrack(0, 0, [])
        return result