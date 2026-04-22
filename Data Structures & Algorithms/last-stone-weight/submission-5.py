import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            c = heapq.heappop(stones) - heapq.heappop(stones)
            if c < 0:
                heapq.heappush(stones, c)
        return -stones[0] if stones else 0