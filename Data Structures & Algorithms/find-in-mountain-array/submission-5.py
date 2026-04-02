class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        l, r = 1, n - 2
        while l <= r:
            m = (l + r) // 2
            a, b, c = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if a < b < c:
                l = m + 1
            elif a > b > c:
                r = m - 1
            else:
                break
        
        peak = m
        
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            h = mountainArr.get(m)
            if h == target:
                return m
            elif h < target:
                l = m + 1
            else:
                r = m - 1
        
        l, r = peak + 1, n - 1
        while l <= r:
            m = (l + r) // 2
            h = mountainArr.get(m)
            if h == target:
                return m
            elif h < target:
                r = m - 1
            else:
                l = m + 1
        
        return -1