import re


class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not re.match(r'^[a-zA-Z0-9]{3,}$', word):  # Use regex to match all letters and digits 3+ times
            return False

        has_vowel = any(c.lower() in 'aeiou' for c in word if c.isalpha())
        has_consonant = any(c.lower() in 'qwrtypsdfghjklzxcvbnm' for c in word)

        return has_vowel and has_consonant