#Resolved
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0   # Iterate over the characters in s

        for c in t:
            # Check if j < len(s) first to handle s being an empty string
            if j < len(s) and c == s[j]:
                j += 1

        # j always ends 1 over the last character it matched
        return j == len(s)