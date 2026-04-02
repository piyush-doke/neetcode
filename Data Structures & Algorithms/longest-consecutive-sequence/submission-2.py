class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)
        for n in nums_set:
            if n - 1 not in nums_set:
                m = n
                while m in nums_set:
                    m += 1
                result = max(m - n, result)
        return result