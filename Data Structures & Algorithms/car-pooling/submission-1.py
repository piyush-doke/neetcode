import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        h = []
        for n, p, d in trips:
            while h and h[0][0] <= p:
                _, seats = heapq.heappop(h)
                capacity += seats
            capacity -= n
            if capacity < 0: return False
            heapq.heappush(h, (d, n))
        return True