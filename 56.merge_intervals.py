class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])
        merged_intervals = []

        start, end = intervals[0]

        for s, e in intervals[1:]:
            if s <= end:
                end = max(e, end)
            else:
                merged_intervals.append([start, end])
                start = s
                end = e

        merged_intervals.append([start, end])

        return merged_intervals
