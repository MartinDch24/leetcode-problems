#Resolved - 2
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0  # The maximum distance we can cover in the array

        for i, jump in enumerate(nums):
            if i > max_reach:  # If i is out of reach, we can't reach the last index
                break
            # Potentially increase max_reach with the current index and it's max jump length
            max_reach = max(max_reach, i + jump)

        return max_reach >= n - 1  # See if we can reach the end of the array