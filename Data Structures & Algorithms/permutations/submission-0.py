class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        h = [False] * len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(curr[:])
            else:
                for i in range(len(nums)):
                    if not h[i]:
                        h[i] = True
                        curr.append(nums[i])
                        backtrack(curr)
                        curr.pop()
                        h[i] = False
        
        backtrack([])
        return result