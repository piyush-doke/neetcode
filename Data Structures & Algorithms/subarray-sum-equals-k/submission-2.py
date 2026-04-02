from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum, count = 0, 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        for n in nums:
            running_sum += n
            count += prefix_sums[running_sum - k]
            prefix_sums[running_sum] += 1
        return count