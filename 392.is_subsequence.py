class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:  # If s is an empty string
            return True
        j = 0  # Track characters in s

        for i in range(len(t)):
            # If we find the current char of s in t, move onto the next one
            if s[j] == t[i]:
                j += 1

                # We've found all characters of s in t
                if j >= len(s):
                    return True

        return False