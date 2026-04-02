class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if sum(map(lambda x: -(-x // m), piles)) <= h:
                r = m
            else:
                l = m + 1
        return r