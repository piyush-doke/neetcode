class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = 0
        right = x // 2
        while left <= right:
            mid = left + (right - left) // 2
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right