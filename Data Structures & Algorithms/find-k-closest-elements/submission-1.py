from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary Search to find x's position in the array
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        left -= 1
        queue = deque()
        for i in range(k):
            a = arr[left] if left >= 0 else float("inf")
            b = arr[right] if right < len(arr) else float("inf")
            if abs(a - x) <= abs(b - x):
                queue.appendleft(a)
                left -= 1
            else:
                queue.append(b)
                right += 1
        
        return list(queue)