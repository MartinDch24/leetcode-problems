#Resolved
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]

                if abs(target - curr_sum) < abs(target - res):
                    res = curr_sum

                if curr_sum < target:
                    j += 1  # Increase sum
                else:
                    k -= 1  # Decrease sum

        return res