class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        pairs = 0

        for i in range(1, n):
            if s[i - 1] == s[i]:
                pairs += 1

        start_end = s[0] == s[-1]  # Wrapping around the prefix will create a new pair if this is True

        if start_end:
            if k == pairs + 1:
                # We cut anywhere around the pairs and create a new one from the wraparound
                return n - (pairs + 1)
            elif k == pairs:
                # We cut 1 of the pairs
                return pairs + 1
        else:
            if k == pairs:
                # Cut anywhere around the pairs
                return n - pairs
            elif k == pairs - 1:
                # Cut any pair
                return pairs

        return 0