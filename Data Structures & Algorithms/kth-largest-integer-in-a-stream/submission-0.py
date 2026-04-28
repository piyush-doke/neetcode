import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        for n in nums:
            if len(self.h) < self.k:
                heapq.heappush(self.h, n)
            else:
                heapq.heappushpop(self.h, n)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            heapq.heappushpop(self.h, val)
        return self.h[0]
