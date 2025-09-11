class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dist = float("inf")
        res = 0

        for i in range(len(nums) - 2):  # Fix the first index in place
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates to have less iterations
                continue

            j, k = i + 1, len(nums) - 1  # Initialize two pointers for the remaining range
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < target:  # If the sum is bellow target, check whether the distance is closer than before
                    if dist > target - total:
                        dist = target - total
                        res = total

                    j += 1  # Shrink from the left

                elif total > target:  # If the sum is larger than target, check the distance
                    if dist > total - target:
                        dist = total - target
                        res = total

                    k -= 1  # Shrink from the right

                else:  # In this case, the sum is equal to the target and the distance is 0, so we just return it
                    return total

        return res