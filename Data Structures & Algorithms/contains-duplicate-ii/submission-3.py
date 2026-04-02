class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()
        for i, n in enumerate(nums):
            if i - hash_map.get(n, float("-inf")) <= k:
                    return True
            hash_map[n] = i
        return False