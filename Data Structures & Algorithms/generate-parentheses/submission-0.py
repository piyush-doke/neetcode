class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open, close, curr):
            if len(curr) == n * 2:
                result.append("".join(curr))
            if open < n:
                curr.append("(")
                open += 1
                backtrack(open, close, curr)
                open -= 1
                curr.pop()
            if close < open:
                curr.append(")")
                close += 1
                backtrack(open, close, curr)
                close -= 1
                curr.pop()

        backtrack(0, 0, [])
        return result