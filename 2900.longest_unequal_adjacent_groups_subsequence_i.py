class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        curr = groups[0]
        n = len(groups)
        res = [words[0]]

        for i in range(n):
            if curr != groups[i]:
                res.append(words[i])
                curr = groups[i]

        return res