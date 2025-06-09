class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        longest_len = 0

        num_indexes = {num: i for i, num in enumerate(arr)}
        fib_len_map = {}
        n = len(arr)

        if not arr:
            return 0

        for i in range(n):
            for j in range(i):
                x = arr[i] - arr[j]
                if x in num_indexes and num_indexes[x] < j:
                    index_of_num = num_indexes[x]
                    fib_len_map[j, i] = fib_len_map.get((index_of_num, j), 2) + 1
                    longest_len = max(longest_len, fib_len_map[j, i])

        return longest_len if longest_len >= 3 else 0


test = Solution()

print(test.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
'''
        index = {num: i for i, num in enumerate(arr)}  # Store number indices for quick lookup
        n = len(arr)
        dp = {}  # Dictionary to store DP states (i, j) -> length of sequence
        
        longest = 0
        
        for j in range(n):
            for i in range(j):
                x = arr[j] - arr[i]  # Find the previous Fibonacci number
                if x in index and index[x] < i:  # Check if x exists and is before arr[i]
                    k = index[x]  # Get index of x
                    dp[i, j] = dp.get((k, i), 2) + 1  # Extend existing sequence or start a new one
                    longest = max(longest, dp[i, j])
        
        return longest if longest >= 3 else 0  # Return 0 if no valid sequence found'''