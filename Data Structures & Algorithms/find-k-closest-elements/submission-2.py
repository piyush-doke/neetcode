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
        for _ in range(k):
            if left < 0:
                queue.append(arr[right])
                right += 1
            elif right >= len(arr):
                queue.appendleft(arr[left])
                left -= 1
            elif x - arr[left] <= arr[right] - x:
                queue.appendleft(arr[left])
                left -= 1
            else:
                queue.append(arr[right])
                right += 1
        
        return list(queue)