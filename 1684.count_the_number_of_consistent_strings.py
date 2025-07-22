from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count = 0  # The count of consistent strings
        allowed = set(allowed)  # Convert allowed into a set for faster lookups

        for word in words:
            for char in word:  # If every character in the word is allowed, than the loop won't break and we'll go into the else block that will increase the count by 1
                if char not in allowed:
                    break
            else:
                count += 1

        return count