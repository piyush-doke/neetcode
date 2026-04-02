class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
  
        for n in numsSet:
            # This number is the start of a sequence
            if n - 1 not in numsSet:
                m = n
                while m in numsSet:
                    m += 1
                longest = max(longest, m - n)

        return longest
