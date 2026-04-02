class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = max_length = 0
        seen = set()
        
        for r in range(len(s)):
            while s[r] in seen and l < r:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_length = max(max_length, r - l + 1)
        
        return max_length