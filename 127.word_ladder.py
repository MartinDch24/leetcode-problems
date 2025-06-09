from collections import deque, defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        q = deque([(beginWord, 1)])
        wordPatterns = defaultdict(list)
        visited = {beginWord}

        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i + 1:]
                wordPatterns[pattern].append(w)

        while q:
            cur_word, count = q.popleft()

            for i in range(len(cur_word)):
                new_pattern = cur_word[:i] + '*' + cur_word[i + 1:]

                if new_pattern in wordPatterns:
                    for w in wordPatterns[new_pattern]:
                        if w == endWord:
                            return count + 1

                        if w not in visited:
                            visited.add(w)
                            q.append((w, count + 1))

        return 0