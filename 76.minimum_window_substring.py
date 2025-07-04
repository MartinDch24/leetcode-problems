from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        t_freq = Counter(t) # {<char>: <times it appears>, ...}
        window = Counter()   # window of {<char>: <times it appears>, ...}, which will change as we move left and right
        have, need_chars = 0, len(t_freq)   # Have is the number of unique characters we have enough of and need is the number of unique characters we need
        res = [-1, -1]  # left and right for the result substring
        res_len = float('inf')  # the smallest length of a substring

        left = 0
        for right in range(len(s)):
            c = s[right]    # Next character
            window[c] += 1  # Increase its frequnecy in the window

            if c in t_freq and window[c] == t_freq[c]:  # If the new needed characters contain the new one and we now have as much of this character as we need, we add +1 to have
                have += 1

            while have == need_chars:   # While the window includes all needed characters for it to be viable
                if (right - left + 1) < res_len:    # We check whether the new length is shorter than the old one
                    res = [left, right] # Add new left and right for the substring
                    res_len = right - left + 1  # Change the min length

                window[s[left]] -= 1    # Remove the left-most character as we shrink the window
                if s[left] in t_freq and window[s[left]] < t_freq[s[left]]: # If the left-most character was one we needed and its not a useless duplicate, we lose 1 of the characters we need, hence have -= 1
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""  # We return a substring, only if we've found a viable substring, which would've caused res_len to change from its inital float('inf'), otherwise we return an empty string