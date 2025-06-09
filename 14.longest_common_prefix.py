class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_word = min(strs, key=len)

        while shortest_word:
            if all(string.startswith(shortest_word) for string in strs):
                return shortest_word

            shortest_word = shortest_word[:-1]
        return ""
