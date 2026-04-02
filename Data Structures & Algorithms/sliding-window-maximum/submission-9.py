from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [0] * (len(nums) - k + 1)
        dq = deque()

        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()

            j = i - k + 1
            if j >= 0:
                result[j] = nums[dq[0]]

        return result