from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:    # So we can initialize the start variable
            return []

        start = nums[0] # The start of the first range will be the first number
        res = []    # Where we'll be saving the ranges

        for i in range(1, len(nums)):   # Start from 1, since we already have start equal to the first number
            if nums[i-1] != nums[i] - 1: # If the previous and current number aren't continuous
                if start == nums[i-1]:  # We check whether our last start value is equal to the previous number, because that would mean the range is only that single number
                    res.append(f"{start}")
                else:
                    res.append(f"{start}->{nums[i-1]}") # Otherwise add the range from start to the previous number

                start = nums[i]

        if start == nums[-1]:   # Check one last time after exiting the loop
            res.append(f"{start}")
        else:
            res.append(f"{start}->{nums[-1]}")

        return res