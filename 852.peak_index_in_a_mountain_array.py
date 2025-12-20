class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1 # Smallest and Largest possible indices of the peak

        while left < right: # When left == right, we've found the peak
            mid = (left + right) // 2   # Candidate index

            # We're on the left slope and must move to the right of mid
            if arr[mid] < arr[mid+1]:
                left = mid+1
            # Otherwise we're either on the right slope, or right on the peak
            else:
                right = mid

        return left # We can also return right, since they're now equal