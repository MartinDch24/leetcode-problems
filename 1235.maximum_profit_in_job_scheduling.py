class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        # Group jobs and sort them by end time
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        jobs.sort(key=lambda x: (x[1], x[0]))

        dp = [0] * (n + 1)  # dp[i] = <largest profit using the first i jobs>

        for i in range(1, n + 1):
            start, end, profit = jobs[i - 1]
            dp[i] = dp[i - 1]  # Skip job i

            # Do binary search on the previous jobs to find the latest job that finishes no later than i's start
            left = 0
            right = i - 1
            while left < right:
                mid = (left + right) // 2
                if jobs[mid][1] <= start:
                    left = mid + 1
                else:
                    right = mid

            # left is now the index of the first incompatibale (i.e. > start) job from left to right, but since the dp array is ofset by one, we can use dp[left] represents the best profit, using jobs from 0 to left-1
            dp[i] = max(dp[i], dp[left] + profit)

        return dp[n]