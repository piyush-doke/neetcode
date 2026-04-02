class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for s in strs[1:]:
            i = 0
            while i < min(len(s), len(prefix)):
                if s[i] != prefix[i]:
                    break
                i += 1
            prefix = prefix[:i]
            if i == 0:
                break
        return prefix