#Resolved - 3
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
                # Skip duplicates
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


        # New Solution:

        # n = len(nums)
        # nums.sort()
        # res = []
        #
        # for i in range(n):
        #     if i > 0 and nums[i - 1] == nums[i]:
        #         continue
        #
        #     j = i + 1
        #     k = n - 1
        #     while j < k:
        #         if nums[j] + nums[k] + nums[i] < 0:
        #             j += 1
        #         elif nums[j] + nums[k] + nums[i] > 0:
        #             k -= 1
        #         else:
        #             res.append([nums[i], nums[j], nums[k]])
        #             j += 1
        #             k -= 1
        #
        #         while i + 1 < j < k and nums[j - 1] == nums[j]:
        #             j += 1
        #             continue
        #         while j < k < n - 1 and nums[k + 1] == nums[k]:
        #             k -= 1
        #             continue
        # return res