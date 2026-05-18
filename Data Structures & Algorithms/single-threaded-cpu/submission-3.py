import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted(enumerate(tasks), key=lambda x: x[1][0])
        
        result = []
        p_heap = []
        time = 0
        i = 0
        
        while i < len(sorted_tasks) or p_heap:
            if not p_heap and sorted_tasks[i][1][0] > time:
                time = sorted_tasks[i][1][0]
            while i < len(sorted_tasks) and sorted_tasks[i][1][0] <= time:
                idx, (enqueue, process) = sorted_tasks[i]
                heapq.heappush(p_heap, (process, idx))
                i += 1
            process, idx = heapq.heappop(p_heap)
            result.append(idx)
            time += process
        
        return result
