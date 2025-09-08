class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r] # The current sum
            if s == target:
                return [l+1, r+1]  # 1-indexed
            elif s < target:    # If it's less than the target, we move l up to increase the sum
                l += 1
            else:   # If it is more, we move the r down to decrease the sum
                r -= 1