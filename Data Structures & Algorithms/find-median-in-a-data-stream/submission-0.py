import heapq

class MedianFinder:
    def __init__(self):
        # max-heap (store negatives for Python’s min-heap)
        self.left = []
        # min-heap
        self.right = []

    def addNum(self, num: int) -> None:
        # Step 1: push to max-heap
        heapq.heappush(self.left, -num)

        # Step 2: balance → largest of left goes to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Step 3: ensure size property
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
