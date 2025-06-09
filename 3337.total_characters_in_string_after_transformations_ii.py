class Solution(object):
    def lengthAfterTransformations(self, s, t, nums):
        """
        :type s: str
        :type t: int
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for _ in range(t):
            next_freq = [0] * 26
            for i in range(26):
                count = freq[i]
                spread = nums[i]
                for j in range(1, spread + 1):
                    idx = (i + j) % 26
                    next_freq[idx] = (next_freq[idx] + count) % MOD
            freq = next_freq

        return sum(freq) % MOD