class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        # Fix the largest side and move the other 2 to satisfy the condition
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1

            while i < j:
                # nums[i] <= nums[j] <= nums[k], that is why we need to check only this condition for the sides to make a triangle
                if nums[i] + nums[j] > nums[k]:
                    res += j - i  # All i-s from i itself up to j-1 would make valdi triplets
                    j -= 1  # Move j down and try to make a triangle again
                else:
                    i += 1  # Increase the value of nums[i] + nums[j]

        return res