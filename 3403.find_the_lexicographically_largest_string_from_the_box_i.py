class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        max_len = len(word) - (numFriends - 1)
        max_word = ""

        for i in range(len(word) - max_len + 1):
            curr = word[i:i + max_len]
            if curr > max_word:
                max_word = curr

        return max_word