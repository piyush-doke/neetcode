class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            for i in range(len(s)):
                j = len(s) - i - 1
                if s[i] != s[j]:
                    return False
            return True
        
        for i in range(len(s)):
            j = len(s) - i - 1
            if s[i] != s[j]:
                return isPalindrome(s[:i] + s[i + 1:]) or isPalindrome(s[:j] + s[j + 1:])
        
        return True