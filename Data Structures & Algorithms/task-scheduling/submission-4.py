from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks).most_common()
        f = freq[0][1]
        m = sum(1 for _, v in freq if v == f)
        idle = (f - 1) * (n - (m - 1)) - (len(tasks) - f * m)
        return len(tasks) + max(idle, 0)
