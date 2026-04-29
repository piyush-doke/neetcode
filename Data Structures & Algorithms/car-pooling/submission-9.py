class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for n, p, d in trips:
            events.append((p, n))
            events.append((d, -n))
        events.sort()
        cur = 0
        for _, change in events:
            cur += change
            if cur > capacity:
                return False
        return True
