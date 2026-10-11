class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        max_len = 0

        i = 1
        start = 0
        while i < n:
            # Keep moving start until we find an ascent
            if arr[i - 1] >= arr[i]:
                start = i
                i += 1
                continue

            # Ascend
            while i < n and arr[i - 1] < arr[i]:
                i += 1

            # Descend
            if i < n and arr[i - 1] > arr[i]:
                while i < n and arr[i - 1] > arr[i]:
                    i += 1

                max_len = max(max_len, i - start)
                start = i - 1  # Move start to the next mountain
            else:
                # Move start if we've found no descent
                start = i
        return max_len