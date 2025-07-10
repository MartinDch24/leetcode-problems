class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None  # Potential candidate to win the "election"
        votes = 0  # The current amount of "votes" it has

        for num in nums:
            if votes == 0:  # If the votes are 0, the new candidate becomes the current number
                candidate = num

            if candidate == num:  # If the current number is the candidate, increase the votes
                votes += 1
            else:  # Otherwise decrease the votes
                votes -= 1

        return candidate