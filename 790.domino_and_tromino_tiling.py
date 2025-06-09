class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2

        dp = [0] * (n + 1)
        t = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        t[2] = 1

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * t[i - 1]) % MOD

            t[i] = (t[i - 1] + dp[i - 2]) % MOD

        return dp[n]

        # dp_dict = dict((k,-1) for k in range(3, n+1))
        # t_dict = dict((k,-1) for k in range(3, n+1))
        #
        # def dp(n):
        #     if n==0: return 1
        #     if n==1: return 1
        #     if n==2: return 2
        #     if dp_dict[n] != -1: return dp_dict[n]
        #     dp_dict[n] = (dp(n-1) + dp(n-2) + 2 * t(n-1)) % MOD
        #     return dp_dict[n]
        #
        # def t(n):
        #     if n <= 1: return 0
        #     if n in t_dict: return t_dict[n]
        #     t_dict[n] = (t(n - 1) + dp(n - 2)) % MOD
        #     return t_dict[n]
        #
        # return dp(n)