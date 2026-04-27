from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        if c.most_common(1)[0][1] > (len(s) + 1) // 2:
            return ""

        heap = [(-v, k) for k, v in c.items()]
        heapq.heapify(heap)
        
        result, prev = [], (0, "")
        while heap:
            v, k = heapq.heappop(heap)
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            result.append(k)
            prev = (v + 1, k)

        return "".join(result)