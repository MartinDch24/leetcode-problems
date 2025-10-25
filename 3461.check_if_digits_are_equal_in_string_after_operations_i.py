class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # A Combination of n elements of class k
        # (How many unique ways there are to choose k elements from n elements)
        def c(n, k):
            res = 1
            for i in range(1, k + 1):
                res = res * (n - i + 1) // i
            return res

        n = len(s)
        # Put every digit in an array as a number for easier access
        arr = list(map(int, s))

        # Last 2 digits
        D1 = D2 = 0

        for i in range(n - 1):
            # How many times the current digit contributes to the last 2 digits
            coef = c(n - 2, i) % 10

            # Use arr[i] to skip the last digit in the array, since it doesn't contribute to the last left digit
            # And use arr[i + 1] to skip the first digit in the array, because it doesn't contribute to the last right digit
            D1 = (D1 + coef * arr[i]) % 10
            D2 = (D2 + coef * arr[i + 1]) % 10

        return D1 == D2

        # O(n^2) solution:

        # temp_s = ""
        #
        # while len(s) > 2:
        #     for i in range(1, len(s)):
        #         temp_s += str((int(s[i-1]) + int(s[i])) % 10)
        #
        #     s = temp_s
        #     temp_s = ""
        #
        # return s[0] == s[1]