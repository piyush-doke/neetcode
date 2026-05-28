class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, curr_sum, curr):
            if curr_sum == target:
                result.append(curr[:])
            elif curr_sum > target:
                return
            else:
                for i in range(start, len(nums)):
                    curr.append(nums[i])
                    backtrack(i, curr_sum + nums[i], curr)
                    curr.pop()

        backtrack(0, 0, [])
        return result