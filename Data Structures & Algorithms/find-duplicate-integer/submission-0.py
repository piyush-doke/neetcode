class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if fast == slow:
                break

        slow = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow