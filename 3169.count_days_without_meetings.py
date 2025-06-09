class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # if not meetings:
        #     return days
        #
        # meetings.sort()
        #
        # prev_end = 0
        # for start, end in meetings:
        #     start = max(start, prev_end + 1)
        #     length = end - start + 1
        #     days -= max(length, 0)
        #     prev_end = max(prev_end, end)
        # return days

        meetings.sort()

        start_day, end_day = meetings[0]

        for start, end in meetings[1:]:
            if start <= end_day:
                end_day = max(end_day, end)
            else:
                days -= end_day - start_day + 1
                start_day = start
                end_day = end

        days -= end_day - start_day + 1

        return days
