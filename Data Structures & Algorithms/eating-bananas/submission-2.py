class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = k = max(piles)
        while l <= r:
            m = (l + r) // 2
            t = sum(map(lambda x: -(-x // m), piles))
            if t <= h:
                r = m - 1
                k = min(k, m)
            else:
                l = m + 1
        return k