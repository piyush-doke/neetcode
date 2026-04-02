class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        start = set()
        
        for n in nums:
            if n - 1 not in nums:
                start.add(n)

        seq = 0
        for n in start:
            m = n
            while m in nums:
                m += 1
            seq = max(seq, m - n)

        return seq
