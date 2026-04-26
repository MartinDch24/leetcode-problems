#Resolved
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        curr_sum = 0

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            # Since the numbers are in ascending order,
            # we can pick a number further left or right to increase or increase the sum, so it can match target
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return [left+1, right+1]    # 1-indexed