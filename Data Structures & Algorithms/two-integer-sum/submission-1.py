class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i, n in enumerate(nums):
            d = target - n
            if d in hash_map:
                return [hash_map[d], i]
            hash_map[n] = i
