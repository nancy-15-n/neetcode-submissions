from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # Remove indices out of current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements (not useful)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Append max for current window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

        