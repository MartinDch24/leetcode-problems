from collections import defaultdict


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        dp = defaultdict(list)

        if s[0].isalpha():
            dp[0] = [s[0].lower(), s[0].upper()]
        else:
            dp[0] = [s[0]]

        for i in range(1, len(s)):
            for prev in dp[i - 1]:
                if s[i].isalpha():
                    #Extend all previous previous strings with either an uppercase and lowercase of the current letter
                    dp[i].append(prev + s[i].upper())
                    dp[i].append(prev + s[i].lower())
                    continue

                # s[i] is not a letter so just extend by it
                dp[i].append(prev + s[i])

        return dp[len(s) - 1]