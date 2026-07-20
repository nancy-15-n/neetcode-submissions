import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        
        while low < high:
            mid = (low + high) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)
            
            if hours <= h:
                high = mid  # try smaller k
            else:
                low = mid + 1  # need faster k
        
        return low
