from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counter = defaultdict(int)
        for c in s1:
            counter[c] += 1
        
        l, unseen = 0, len(s1)
        
        for r in range(len(s2)):
            # include s2[r] in the window
            if counter[s2[r]] > 0:
                unseen -= 1
            counter[s2[r]] -= 1
            
            # if window size exceeds, shrink from left
            if r - l + 1 > len(s1):
                counter[s2[l]] += 1
                if counter[s2[l]] > 0:
                    unseen += 1
                l += 1
            
            if unseen == 0:
                return True
        
        return False