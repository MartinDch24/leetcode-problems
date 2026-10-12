class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        n = len(arr)
        min_dist = float('inf')

        res = []
        for i in range(1, n):
            diff = arr[i] - arr[i-1]
            if diff < min_dist:
                res = [[arr[i-1], arr[i]]]
                min_dist = diff
            elif diff == min_dist:
                res.append([arr[i-1], arr[i]])
        return res