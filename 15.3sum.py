#Resolved
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Remove duplicates
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                # Take -nums[i] as a target sum for nums[j] + nums[k]
                if nums[j] + nums[k] == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])

                    # Remove duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1

                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1  # Increase sum
                else:
                    k -= 1  # Decrease sum

        return res