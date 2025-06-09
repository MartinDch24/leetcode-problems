import re

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        pattern = r'^\s*([+-]?\d+)'
        match = re.match(pattern, s)

        if not match:
            return 0

        num = int(match.group(1))

        MIN_INT, MAX_INT = -2 ** 31, 2 ** 31 - 1

        return max(MIN_INT, min(num, MAX_INT))