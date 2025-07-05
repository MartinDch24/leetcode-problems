import heapq


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_heap = []  # Priority queue (heap), that will keep the largest values at the beginning of the queue
        res = []

        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i],
                                      i))  # We start pushing each number, along with it's index. We use -nums[i], because heapq is a min priority queue by default

            if i >= k - 1:  # When i reaches the minum size of a subarray
                while max_heap[0][1] <= i - k:  # While the index not in the current window
                    heapq.heappop(max_heap)  # Remove the top element

                res.append(-max_heap[0][0])  # Append the new top of the queue to the result

        return res