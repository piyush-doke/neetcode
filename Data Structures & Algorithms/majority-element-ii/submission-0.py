class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = None
        m1 = m2 = 0
        for n in nums:
            if n == c1:
                m1 += 1
            elif n == c2:
                m2 += 1
            elif m1 == 0:
                c1 = n
                m1 = 1
            elif m2 == 0:
                c2 = n
                m2 = 1
            else:
                m1 -= 1
                m2 -= 1
        
        f1 = f2 = 0
        for n in nums:
            if n == c1:
                f1 += 1
            elif n == c2:
                f2 += 1
        
        result = []
        if f1 > len(nums) // 3:
            result.append(c1)
        if f2 > len(nums) // 3:
            result.append(c2)
        return result