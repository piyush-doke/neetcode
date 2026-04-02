class Solution:
    def trap(self, height: List[int]) -> int:
        tallest = 0
        right = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            right[i] = tallest
            tallest = max(tallest, height[i])

        area = tallest = 0
        for i, h in enumerate(height):
            area += max(min(tallest, right[i]) - h, 0)
            tallest = max(tallest, h)
        return area
