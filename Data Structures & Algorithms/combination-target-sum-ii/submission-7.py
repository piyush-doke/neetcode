class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, curr_sum, curr):
            if curr_sum == target:
                result.append(curr[:])
            elif curr_sum < target:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    curr.append(candidates[i])
                    backtrack(i + 1, curr_sum + candidates[i], curr)
                    curr.pop()
            else:
                return
            
        
        backtrack(0, 0, [])
        return result