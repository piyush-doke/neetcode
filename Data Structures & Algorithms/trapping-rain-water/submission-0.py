class Solution:
    def trap(self, height: List[int]) -> int:
        leftWall = [0] * len(height)
        tallest = height[0]
        
        for i in range(1, len(height)):
            leftWall[i], tallest = tallest, max(tallest, height[i])

        water = 0
        tallest = height[-1]
        for i in range(len(height) - 2, -1, -1):
            water += max(min(leftWall[i], tallest) - height[i], 0)
            tallest = max(tallest, height[i])
        
        return water

        