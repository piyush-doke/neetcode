class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if stack and pairs.get(c) == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0
