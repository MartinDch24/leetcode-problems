class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        '''
        Idea: subarrays where sum == goal are
        <subarrays where sum <= goal> - <subarrays where sum <= goal-1>
        '''

        left = 0
        curr_sum = 0
        count1 = 0  # Subarrays where sum <= goal

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > goal:
                curr_sum -= nums[left]
                left += 1

            count1 += right - left + 1

        # goal - 1 would be negative, so count2 = 0
        if goal <= 0:
            return count1

        left = 0
        curr_sum = 0
        count2 = 0  # Subarrays where sum <= goal - 1

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > goal - 1:
                curr_sum -= nums[left]
                left += 1

            count2 += right - left + 1

        return count1 - count2