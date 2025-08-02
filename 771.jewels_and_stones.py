class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)  # Convert jewels to a set for faster look-ups
        count = 0  # How many stones are jewels

        for s in stones:
            if s in jewels:
                count += 1

        return count