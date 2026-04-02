class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            m = (l + r) // 2
            m2 = m * m
            if m2 < x:
                l = m + 1
            elif m2 > x:
                r = m - 1
            else:
                return m

        return r