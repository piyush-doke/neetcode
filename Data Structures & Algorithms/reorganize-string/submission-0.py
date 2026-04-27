from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        if c.most_common(1)[0][1] > (len(s) + 1) // 2:
            return ""

        heap = [(-v, k) for k, v in c.items()]
        heapq.heapify(heap)
        
        result = []
        prev = ""
        while len(result) < len(s):
            v1, k1 = heapq.heappop(heap)
            if k1 == prev:
                v2, k2 = v1, k1
                v1, k1 = heapq.heappop(heap)
                heapq.heappush(heap, (v2, k2))
            result.append(k1)
            if -v1 > 0:
                heapq.heappush(heap, (v1 + 1, k1))
            prev = k1

        return "".join(result)