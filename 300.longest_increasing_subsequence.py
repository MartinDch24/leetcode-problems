#Resolved - 2
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Binary search O(n log n) solution:

        # tails[i] = <the smallest number subsequence of length i+1 can end on>
        tails = []

        for num in nums:
            # Find from where num can extend a subsequence
            idx = bisect_left(tails, num)

            # if idx == len(tails), then it's the largest tail yet and goes at the end of the list
            if idx < len(tails):
                tails[idx] = num
            else:
                tails.append(num)

        # tails does not necessarily contain the actual LIS,
        # but its length is always the LIS length
        # because the existence of tails[i] guarantees the existence of a subsequence of len i+1
        return len(tails)

        # DP solution:
        # n = len(nums)
        # longest = [1] * n # Longest strictly increasing subsequence ending at i
        #
        # for i in range(n):
        #     # Use longest[j], where nums[j] < nums[i] and longest[j] is the largest candidate
        #     longest[i] = max((longest[j] for j in range(i) if nums[j] < nums[i]), default=0) + 1 # Add 1 to extend the sequence
        #
        # return max(longest) # Return the longest sequence