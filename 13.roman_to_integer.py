class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total_sum = roman_to_num[s[0]]

        for i in range(1, len(s)):
            current_val = roman_to_num[s[i]]
            prev_val = roman_to_num[s[i - 1]]

            if current_val > prev_val:
                total_sum += current_val - 2 * prev_val
            else:
                total_sum += current_val

        return total_sum