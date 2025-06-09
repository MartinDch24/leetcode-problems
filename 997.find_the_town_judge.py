class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_scores = [0] * n

        for a, b in trust:
            trust_scores[a-1] -= 1
            trust_scores[b-1] += 1

        if n-1 in trust_scores:
            return trust_scores.index(n-1)+1

        return -1