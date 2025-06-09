class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        MOD = 10**9 + 7
        freq = [0 for _ in range(26)]
        ascii_a = ord("a")

        for char in s:
            freq[ord(char) - ascii_a] += 1
        for _ in range(t):
            freq.insert(0, freq.pop())
            freq[1]+=freq[0]

        return sum(freq)%MOD

        # MOD = 10 ** 9 + 7
        # freq = [0] * 26
        #
        # for ch in s:
        #     freq[ord(ch) - ord('a')] += 1
        #
        # for _ in range(t):
        #     next_freq = [0] * 26
        #     for i in range(26):
        #         if i == 25:
        #             next_freq[0] = (next_freq[0] + freq[i]) % MOD
        #             next_freq[1] = (next_freq[1] + freq[i]) % MOD
        #         else:
        #             next_freq[i + 1] = (next_freq[i + 1] + freq[i]) % MOD
        #     freq = next_freq
        #
        # return sum(freq) % MOD