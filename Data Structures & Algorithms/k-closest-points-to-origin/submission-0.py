import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min-heap based on squared distance
        heap = []
        for (x, y) in points:
            dist = x*x + y*y
            heapq.heappush(heap, (dist, [x, y]))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
