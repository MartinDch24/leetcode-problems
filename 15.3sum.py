class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:  # If the current number is the same as the previous, we'd have duplicate
                continue

            j, k = i+1, len(nums)-1 # We make a window with the left end being the first index+1 and the last index 
            while j < k:
                if nums[j] + nums[k] == -nums[i]:   # We check whether the total sum is 0
                    res.append([nums[i], nums[j], nums[k]]) # Add the numbers to the result

                    while j < k and nums[j] == nums[j+1]:   # Since the list is sorted, we can just push j and k in, until we skip all possible duplicates
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1  # Increase the sum of the 2nd and 3rd number, by shrinking the left end of the window
                else:
                    k -= 1  # Decrease the sum of 2nd and 3rd number, by shrinking the right end

        return res