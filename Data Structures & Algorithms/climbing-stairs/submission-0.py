class Solution:
    def climbStairs(self, n: int) -> int:
        left, right = 1, 2
        if n == 1:
            return left
        
        for _ in range(2, n):
            temp = left + right
            left = right
            right = temp
        
        return right
