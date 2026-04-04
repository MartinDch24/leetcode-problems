class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
    ### Core idea: Mark 0s as -1 and 1s as 1 then track a prefix sum. When the sum is 0, we have an equal amount of 0s and 1s

        prefix_index = {0: -1}  # Save the earliest index where we find each prefix sum
        curr_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            curr_sum += 1 if num == 1 else -1

            # If the same prefix sum appears at indices j and i,
            # then the subarray (j+1 to i) has an equal amount of 0s and 1s
            if curr_sum in prefix_index:
                max_len = max(max_len,  i - prefix_index[curr_sum])
            else:
                prefix_index[curr_sum] = i

        return max_len