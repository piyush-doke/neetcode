class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = dict()
        for i in range(len(nums)):
            j = memory.get(target - nums[i], -1)
            if j >= 0:
                return [j, i]
            memory[nums[i]] = i