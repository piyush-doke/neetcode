from random import randint
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(l, r):
            if l >= r:
                return
            
            k = randint(l, r)
            nums[k], nums[r] = nums[r], nums[k]
            p = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] < p:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            
            quickSort(l, i - 1)
            quickSort(i + 1, r)
        
        quickSort(0, len(nums) - 1)
        return nums
