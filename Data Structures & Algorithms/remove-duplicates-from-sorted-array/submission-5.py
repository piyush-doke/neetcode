class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = slow = 0
        while fast < len(nums):
            nums[slow] = nums[fast]
            fast += 1
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1
            slow += 1
        return slow