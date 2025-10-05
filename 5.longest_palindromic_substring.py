class Solution:
    def longestPalindrome(self, s: str) -> str:
        #DP solution:

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1   # The start index of the result starts with 0 and the max length with 1

        for i in range(n):
            dp[i][i] = True

        # Build shorter substrings first then move on to longer ones
        for i in range(n - 1, -1, -1):  # Go backwards
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # j - i == 1 means that the substring has 2 identical characters
                    # dp[i+1][j-1] checks if the inside is palindromic before adding the 2 new characters on the left and right
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        # j-i+1 is the length of the new palindrome, so we compare it with max_len so far
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            start = i

        return s[start:start + max_len]

        # n = len(s)
        # max_len = 0
        #
        # def expandAroundCenter(left, right):
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     return s[left + 1:right]
        #
        # longest = ""
        # for i in range(n):
        #     substr1 = expandAroundCenter(i, i)
        #     substr2 = expandAroundCenter(i, i + 1)
        #
        #     if len(longest) < len(substr1):
        #         longest = substr1
        #     if len(longest) < len(substr2):
        #         longest = substr2
        #
        # return longest