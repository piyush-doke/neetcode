class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()
        
        for i in range(len(nums)):
            if i - hash_map.get(nums[i], float("-inf")) <= k:
                return True
            hash_map[nums[i]] = i
        
        return False