class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            l = i
            while stack and stack[-1][1] > h:
                l, height = stack.pop()
                max_area = max(max_area, height * (i - l))
            stack.append((l, h))

        for l, h in stack:
            max_area = max(max_area, h * (len(heights) - l))

        return max_area