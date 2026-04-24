from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        f = m = 0
        for t in tasks:
            freq[t] += 1
            if freq[t] > f:
                f = freq[t]
                m = 1
            elif freq[t] == f:
                m += 1
        idle = (f - 1) * (n - (m - 1)) - len(tasks) + f * m
        return len(tasks) + max(idle, 0)