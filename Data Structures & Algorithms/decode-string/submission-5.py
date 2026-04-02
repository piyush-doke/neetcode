class Solution:
    def decodeString(self, s: str) -> str:
        decoded = ""
        repeat = 0
        stack = []
        for c in s:
            if c.isdigit():
                repeat = repeat * 10 + int(c)
            elif c == "[":
                stack.append((decoded, repeat))
                decoded = ""
                repeat = 0
            elif c == "]":
                last_decoded, last_repeat = stack.pop()
                decoded = last_decoded + decoded * last_repeat
            else:
                decoded += c
        
        return decoded