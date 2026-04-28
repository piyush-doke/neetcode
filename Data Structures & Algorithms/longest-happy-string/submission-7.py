import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = [(-f, c) for f, c in [(a, "a"), (b, "b"), (c, "c")] if f > 0]
        heapq.heapify(h)

        result = []
        while h:
            f1, c1 = heapq.heappop(h)
            
            if len(result) > 1 and result[-1] == result[-2] == c1:
                if not h:
                    break 
                prev = (f1, c1)
                f1, c1 = heapq.heappop(h)
                heapq.heappush(h, prev)
            
            result.append(c1)
            
            if f1 < -1:
                heapq.heappush(h, (f1 + 1, c1))
        
        return "".join(result)