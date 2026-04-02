from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        length = len(s1)
        left = 0

        for c in s1:
            count[c] += 1

        for right in range(len(s2)):
            
            count[s2[right]] -= 1
            if count[s2[right]] >= 0:
                length -= 1

            if length == 0:
                return True

            if right - left + 1 == len(s1):
                count[s2[left]] += 1
                if count[s2[left]] > 0:
                    length += 1
                left += 1

        return False