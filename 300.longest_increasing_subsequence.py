class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        longest = [1] * n # Longest strictly increasing subsequence ending at i

        for i in range(n):
            # Use longest[j], where nums[j] < nums[i] and longest[j] is the largest candidate
            longest[i] = max((longest[j] for j in range(i) if nums[j] < nums[i]), default=0) + 1 # Add 1 to extend the sequence

        return max(longest) # Return the longest sequence