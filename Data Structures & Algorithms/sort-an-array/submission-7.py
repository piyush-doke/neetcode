from random import randint
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(start, end):
            if start >= end:
                return
            
            rand_index = randint(start, end)
            nums[rand_index], nums[end] = nums[end], nums[rand_index]
           
            pivot = nums[end]
            l, r = start, end - 1
            while l <= r:
                if nums[l] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                    r -= 1
                else:
                    l += 1
            nums[end], nums[l] = nums[l], nums[end]
            
            quickSort(start, l - 1)
            quickSort(l + 1, end)

        quickSort(0, len(nums) - 1)
        return nums
