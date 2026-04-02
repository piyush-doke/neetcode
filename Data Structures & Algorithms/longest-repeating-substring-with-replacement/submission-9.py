from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = majority_count = max_length = 0
        counter = defaultdict(int)
        
        for r in range(len(s)):
            counter[s[r]] += 1
            majority_count = max(majority_count, counter[s[r]])

            while (r - l + 1) - majority_count > k:
                counter[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length
