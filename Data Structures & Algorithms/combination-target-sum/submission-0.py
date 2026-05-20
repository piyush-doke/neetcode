class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, curr, curr_sum):
            if curr_sum == target:
                result.append(curr[:])
            elif curr_sum < target:
                for i in range(start, len(nums)):
                    curr.append(nums[i])
                    curr_sum += nums[i]
                    backtrack(i, curr, curr_sum)
                    curr_sum -= nums[i]
                    curr.pop()
        
        backtrack(0, [], 0)
        return result
