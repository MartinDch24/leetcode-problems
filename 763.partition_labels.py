class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        interval_lens = []
        char_pos = {}

        for i, char in enumerate(s):
            char_pos[char] = i

        start = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end, char_pos[char])

            if i == end:
                interval_lens.append(i - start + 1)
                start = i + 1

        return interval_lens