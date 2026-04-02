class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        for j in range(len(nums)):
            nums[i] = nums[j]
            if nums[i] != val:
                i += 1

        return i