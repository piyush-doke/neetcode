from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums))]
        for key, value in freq.items():
            buckets[value - 1].append(key)
        
        result = []
        for i in range(len(nums) - 1, -1, -1):
            j = len(buckets[i]) - 1
            while j >= 0:
                result.append(buckets[i][j])
                if len(result) == k:
                    return result
                j -= 1
