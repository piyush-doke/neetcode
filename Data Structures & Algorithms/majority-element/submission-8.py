class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = v = 0
        for n in nums:
            if m == n:
                v += 1
            elif v == 0:
                m = n
                v += 1
            else:
                v -= 1
        return m
