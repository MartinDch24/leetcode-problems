from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_count = Counter(s)   # {letter1: it's count, letter2: it's count, ...}
        max_len = 0
        mid_used = False    # Whether we have a letter in the middle or not

        for c in letter_count.values():
            max_len += c//2  # Add as many pairs of a given letter as possible

            if not mid_used and c % 2 != 0: # If we haven't used a middle letter and the current count is an odd number. We can take a single letter from it and put it in the middle
                mid_used = True

        return max_len * 2 + 1 if mid_used else max_len * 2 # Since I've been adding only the number of pairs to max_len, I have to multiply it by 2 and add 1 if we have a letter in the middle
