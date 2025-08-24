class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: # If there is only one person, you can't split the string in any way
            return word

        max_len = len(word) - (numFriends - 1)  # The longest possible substring
        max_word = ""

        for i in range(len(word) - max_len + 1):    # Iterate from 0 up to the last possible start of a max_len substring
            curr = word[i:i + max_len]
            if curr > max_word:
                max_word = curr

        # Check suffixes shorter than max_len
        for i in range(len(word) - max_len + 1, len(word)):
            curr = word[i:]
            if curr > max_word:
                max_word = curr

        return max_word