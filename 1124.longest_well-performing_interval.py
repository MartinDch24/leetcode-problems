#Resolved
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # The sum of tiring and non-tiring days, where they are counted as 1 and -1, respectively
        balance = 0
        res = 0
        first = {}   # Save the first occurrence of a given balance

        for i, time in enumerate(hours):
            balance += 1 if time > 8 else -1

            if balance > 0:
                res = i + 1

            if balance not in first:
                first[balance] = i

            # We are looking for an old balance that was < balance
            if balance - 1 in first:
                res = max(res, i - first[balance - 1])

        return res