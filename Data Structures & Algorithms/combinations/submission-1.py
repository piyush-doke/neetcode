class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, k, curr):
            if k == 0:
                result.append(curr[:])
            else:
                for i in range(start, n + 1):
                    curr.append(i)
                    backtrack(i + 1, k - 1, curr)
                    curr.pop()


        backtrack(1, k, [])
        return result