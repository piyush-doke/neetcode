import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, left, right):
            if left >= right:
                return

            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]

            quickSort(nums, left, i - 1)
            quickSort(nums, i + 1, right)
            return

        quickSort(nums, 0, len(nums) - 1)
        return nums