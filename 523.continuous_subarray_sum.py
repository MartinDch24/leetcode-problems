#Resolved
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = {
            0: -1}  # Initialize with remainder 0 at index -1 so subarrays starting at index 0 can be considered
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            mod = curr_sum % k

            # Check if we've had the same mod of k on the prefix sum at a previous index
            if mod in prefix_mod:
                # Check subarray length is at least 2
                if i - prefix_mod[mod] >= 2:
                    return True

            else:
                # Store the earliest occurrence of a sum with this mod of k, so we can form the longest possible subarray
                prefix_mod[mod] = i

        return False