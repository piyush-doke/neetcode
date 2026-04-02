class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()
        for i, n in enumerate(nums):
            if n in hash_map and i - hash_map[n] <= k:
                return True
            hash_map[n] = i
        return False