from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)

        for n, f in freq.items():
            heapq.heappush(heap, (-f, n))
        
        result = [0] * k
        for i in range(k):
            f, n = heapq.heappop(heap)
            result[i] = n
        return result