class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_needed(cap):
            days, total = 1, 0
            for w in weights:
                if w + total > cap:
                    days += 1
                    total = 0
                total += w
            return days

        l, r = max(weights), sum(weights)
        while l < r:
            m = (l + r) // 2
            if days_needed(m) <= days:
                r = m
            else:
                l = m + 1
        
        return l