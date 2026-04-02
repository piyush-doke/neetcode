from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        counter = defaultdict(int)
        for c in t:
            counter[c] += 1
        
        l = 0
        length = len(t)
        result = ""
        for r in range(len(s)):

            counter[s[r]] -= 1
            if counter[s[r]] >= 0:
                length -= 1

            while length == 0:
                if not result or r - l + 1 < len(result):
                    result = s[l: r + 1]

                counter[s[l]] += 1
                if counter[s[l]] > 0:
                    length += 1
                l += 1

        return result