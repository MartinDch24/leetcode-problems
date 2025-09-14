class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for a in range(n - 3):
            if a > 0 and nums[a - 1] == nums[a]:  # If the current nums[a] is the same number as the previous, skip it
                continue

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:  # If the current nums[b] is the same as nums[b-1], skip it
                    continue

                c, d = b + 1, n - 1  # Initialize a window from b+1 to the end of the array
                while c < d:  # While the indices are valid
                    c_and_d = nums[c] + nums[d]  # The sum of nums[c] and nums[d]
                    goal_sum = target - nums[a] - nums[b]  # The sum that nums[c] + nums[d] should be

                    if c_and_d < goal_sum:
                        # If the sum we have is less than expected, shrink the window from the left
                        # Since the array is sorted, that will increase the current sum
                        c += 1
                    elif c_and_d > goal_sum:
                        # If it is more than expected, just shrink the window from the right
                        d -= 1
                    else:
                        # If the sum is right on, save the numbers in result and shrink the window from both sides
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1

                        # Remove duplicates after finding a valid result
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1

        return res