class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, target, curr):
            if target == 0:
                result.append(curr[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, target - candidates[i], curr)
                curr.pop()

        backtrack(0, target, [])
        return result
