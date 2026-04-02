class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == "..":
                stack and stack.pop()
            elif p and p != ".":
                stack.append(p)
        return "/" + "/".join(stack)
