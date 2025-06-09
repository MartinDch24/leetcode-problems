from collections import deque

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = len(dominoes)
        res = list(dominoes)
        force = [None] * n
        time = [-1] * n
        q = deque()

        for i, char in enumerate(dominoes):
            if char in 'LR':
                q.append ((i, char, 0))
                time[i] = 0
                force[i] = char

        while q:
            idx, char, t = q.popleft()
            next_idx = idx + (1 if char=='R' else -1)

            if 0 <= next_idx < n:
                if time[next_idx] == -1:
                    q.append((next_idx, char, t+1))
                    time[next_idx] = t + 1
                    force[next_idx] = char
                    res[next_idx] = char

                elif time[next_idx] == t + 1 and force[next_idx] != char:
                    res[next_idx] = '.'

        return ''.join(res)

    #         prev = ''
    #         while prev != dominoes:
    #             prev = dominoes
    #             dominoes = dominoes.replace('R.L', 'xxx').replace('.L', 'LL').replace('R.', 'RR')
    #
    #         return dominoes.replace('xxx', 'R.L')