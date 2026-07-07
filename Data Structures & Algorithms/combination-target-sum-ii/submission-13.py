class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, total, curr):
            if total == target:
                result.append(curr[:])
            elif total < target:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    curr.append(candidates[i])
                    backtrack(i + 1, total + candidates[i], curr)
                    curr.pop()

        candidates.sort()
        result = []
        backtrack(0, 0, [])
        return result