import bisect
from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        r = bisect.bisect_left(arr, x)
        l = r - 1
        dq = deque()

        while len(dq) < k:
            if 0 <= l and r < len(arr):
                if x - arr[l] <= arr[r] - x:
                    dq.appendleft(arr[l])
                    l -= 1
                else:
                    dq.append(arr[r])
                    r += 1
            elif 0 <= l:
                dq.appendleft(arr[l])
                l -= 1
            else:
                dq.append(arr[r])
                r += 1
    
        return list(dq)