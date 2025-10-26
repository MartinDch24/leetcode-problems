class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPred(w1, w2):  # See whether w1 is a predecessor to w2
            if len(w2) != len(w1) + 1:  # w2 should be 1 character longer than w1
                return False

            stack = list(w1[::-1])  # Convert the characters of w1 into a reversed stack

            # To maintain order, check each character of w2 and see whether it mataches the current top of the stack
            # If does, pop the character from the stack and keep going
            # If the order of the characters in the words is not maintained
            # Or w2 has more than 1 new character, the stack won't be empty at the end
            for ch in w2:
                if stack and ch == stack[-1]:
                    stack.pop()

            return not stack

        words.sort(key=len)  # Make the words go from shortest to longest

        n = len(words)
        dp = [1] * n  # dp[i] = longest word chain ending at words[i]

        for i in range(n):
            # Extend dp[i], through dp[j], where dp[j] is the longest word chain ending at words[j] and words[j] is a predecessor to words[i]
            dp[i] = 1 + max((dp[j] for j in range(i) if isPred(words[j], words[i])), default=0)

        return max(dp)  # Return the longest found chain