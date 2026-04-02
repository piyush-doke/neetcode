class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m1 = m2 = 0
        v1 = v2 = 0
        for num in nums:
            if num == m1:
                v1 += 1
            elif num == m2:
                v2 += 1
            elif v1 == 0:
                m1 = num
                v1 = 1
            elif v2 == 0:
                m2 = num
                v2 = 1
            else:
                v1 -= 1
                v2 -= 1
        
        c1 = c2 = 0
        for num in nums:
            if num == m1:
                c1 += 1
            elif num == m2:
                c2 += 1

        result = []
        threshold = len(nums) // 3
        if c1 > threshold:
            result.append(m1)
        if c2 > threshold:
            result.append(m2)
        return result