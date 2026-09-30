import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # Make sure the largest numbers make it over to the right heap
        heapq.heappush_max(self.left, num)
        heapq.heappush(self.right, heapq.heappop_max(self.left))

        # Make the left heap always >= to the right
        if len(self.right) > len(self.left):
            heapq.heappush_max(self.left, heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0]
        return (self.left[0] + self.right[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()