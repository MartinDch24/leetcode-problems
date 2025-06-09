from collections import deque


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        q = deque([(n, 0)])
        visited = {n}

        while q:
            cur, count = q.popleft()

            i = 1
            while i ** 2 <= cur:
                next_val = cur - i ** 2

                if next_val == 0:
                    return count + 1
                if next_val not in visited:
                    visited.add(next_val)
                    q.append((next_val, count + 1))

                i += 1