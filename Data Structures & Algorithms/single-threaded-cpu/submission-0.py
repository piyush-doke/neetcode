import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        e_heap = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        heapq.heapify(e_heap)

        p_heap = []
        result = []
        time = 0
        while p_heap or e_heap:
            while e_heap and e_heap[0][0] <= time:
                e, p, i = heapq.heappop(e_heap)
                heapq.heappush(p_heap, (p, i))
            if p_heap:
                p, i = heapq.heappop(p_heap)
                result.append(i)
                time += p
            else:
                time = e_heap[0][0]
        return result