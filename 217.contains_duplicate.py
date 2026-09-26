class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()    # Collect characters we've already seen in a set for O(1) look-ups

        for num in nums:
            # Check if the current number is a duplicate
            if num in seen:
                return True
            else:
                seen.add(num)
        return False