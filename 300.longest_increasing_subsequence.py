from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Binary search O(n log n) solution:

        tails = []  # tails[i] = the smallest num that is the end of a subsequence of length i+1
        for num in nums:
            # Find the smallest possible number the new num can replace to make that tail smaller
            idx = bisect_left(tails, num)
            # If the number fits at the end of the array, append it
            if idx == len(tails):
                tails.append(num)
            else:
                # Otherwise replace the end of a subsequence of length idx+1 with the new, smaller end
                tails[idx] = num

        return len(tails)   # The length of the array is the length of the longest subsequence

        # DP solution:
        # n = len(nums)
        # longest = [1] * n # Longest strictly increasing subsequence ending at i
        #
        # for i in range(n):
        #     # Use longest[j], where nums[j] < nums[i] and longest[j] is the largest candidate
        #     longest[i] = max((longest[j] for j in range(i) if nums[j] < nums[i]), default=0) + 1 # Add 1 to extend the sequence
        #
        # return max(longest) # Return the longest sequence