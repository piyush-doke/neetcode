class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = 0
        v = 0

        for n in nums:
            if v == 0:
                m = n

            if n == m:
                v += 1
            else:
                v -= 1

        return m
