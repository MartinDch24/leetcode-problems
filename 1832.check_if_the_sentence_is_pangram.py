class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26 # Make a set of all characters in the sentence and return true or false if they are 26