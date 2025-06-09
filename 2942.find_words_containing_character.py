class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        n = len(words)

        idxs = []

        for i in range(n):
            if x in words[i]:
                idxs.append(i)

        return idxs