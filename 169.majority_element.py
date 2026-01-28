#Resolved - 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #O(n) time, O(1) space solution:
        '''
        If an element appears more than all other elements combined, it cannot be canceled out completely.
        Matching elements increase the count, mismatches decrease it.
        The true majority can never be fully canceled out.
        '''
        candidate = None
        count = 0

        for num in nums:
            # Switch candidate
            if count == 0:
                candidate = num

            # Reinforce element
            if candidate == num:
                count += 1
            # Decrease majority of the current candidate
            else:
                count -= 1

        return candidate

        #Sorting solution:
        # nums.sort()
        # return nums[len(nums)//2]