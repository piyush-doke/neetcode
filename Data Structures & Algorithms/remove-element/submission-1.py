class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            nums[slow] = nums[fast]
            if nums[slow] != val:
                slow += 1
        return slow