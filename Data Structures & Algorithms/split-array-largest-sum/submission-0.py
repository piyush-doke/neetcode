class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splits(max_sum):
            total, n_splits = 0, 1
            for n in nums:
                if total + n > max_sum:
                    total = 0
                    n_splits += 1
                total += n
            return n_splits

        l, r = max(nums), sum(nums)
        while l < r:
            max_sum = (l + r) // 2
            n_splits = splits(max_sum)
            if n_splits <= k:
                r = max_sum
            else:
                l = max_sum + 1
        return l