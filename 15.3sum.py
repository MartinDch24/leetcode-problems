#Resolved - 2
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            # Skip duplicates
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, n - 2):
                # Skip dublicates
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                # Search on the sum of nums[k] and nums[l]
                k, l = j + 1, n - 1
                needed_sum = target - nums[i] - nums[j]

                while k < l:
                    if nums[k] + nums[l] < needed_sum:
                        k += 1  # Increase sum
                    elif nums[k] + nums[l] > needed_sum:
                        l -= 1  # Decrease sum
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])

                        # Skip duplicates
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l - 1] == nums[l]:
                            l -= 1

                        k += 1
                        l -= 1

        return res