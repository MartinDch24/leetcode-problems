from collections import defaultdict
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        eq_count = defaultdict(int)

        for a,b in dominoes:
            key = a*10+b if a>b else b*10+a
            eq_count[key] +=1

        res = 0
        for i in eq_count.values():
            res += i * (i-1) // 2
        return res