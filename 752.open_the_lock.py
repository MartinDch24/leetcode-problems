from collections import deque


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def get_vars(num):
            res = []
            for i in range(4):
                digit = int(num[i])
                for delta in [-1, 1]:
                    new_digit = (digit + delta) % 10
                    new_num = num[:i] + str(new_digit) + num[i+1:]
                    res.append(new_num)
            return res

        q = deque(['0000'])
        visited = set(deadends)
        turns = 0

        if '0000' in visited:
            return -1

        while q:
            for _ in range(len(q)):
                current = q.popleft()
                if current == target:
                    return turns
                for num in get_vars(current):
                    if num in visited:
                        continue

                    visited.add(num)
                    q.append(num)
            turns += 1

        return -1