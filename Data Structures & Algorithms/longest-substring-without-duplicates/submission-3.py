class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p = result = 0
        seen = set()
        for i, c in enumerate(s):
            if c in seen:
                result = max(result, i - p)
                while s[p] != c:
                    seen.remove(s[p])
                    p += 1
                p += 1
            seen.add(c)
        result = max(result, len(s) - p)
        return result