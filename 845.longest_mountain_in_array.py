class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        start = 0
        max_len = 0

        i = 1
        while i < n:
            # We can't start a mountain while the numbers are still equal or descending
            if arr[i-1] >= arr[i]:
                start = i
                i += 1
                continue

            # Ascend
            while i < n and arr[i-1] < arr[i]:
                i += 1
            if i < n and arr[i-1] > arr[i]:
                # Descend
                while i < n and arr[i-1] > arr[i]:
                    i += 1

                # i is the index immediately after the mountain
                # so the length of it is i - start
                max_len = max(max_len, i-start)
            else:
                # reset if there wasn't a descent
                start = i-1

        return max_len