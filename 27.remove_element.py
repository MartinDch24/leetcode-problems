#Resolved
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0  # The index where the next non-val element should be placed

        for j in range(n):
            # If nums[j] is not val, move it to the next valid position
            if nums[j] != val:
                # Change the next number in-line
                nums[i] = nums[j]
                i += 1

        return i  # Number of elements not equal to val