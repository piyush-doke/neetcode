class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                decoded = []
                while stack[-1] != "[":
                    decoded.append(stack.pop())
                stack.pop()

                base = 1
                repeat = 0
                while stack and stack[-1].isdigit():
                    repeat = int(stack.pop()) * base + repeat
                    base *= 10

                decoded.reverse()
                stack.extend(decoded * repeat)
            else:
                stack.append(c)

        return "".join(stack)