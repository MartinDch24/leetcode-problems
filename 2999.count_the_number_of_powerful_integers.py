class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        max_prefix_len = len(str(finish)) - len_s
        count = [0]

        def backtrack(prefix, depth):
            if depth > max_prefix_len:
                return
            candidate = int(prefix + s)
            if start <= candidate <= finish:
                count[0] += 1
            for digit in range(0, limit + 1):
                backtrack(prefix + str(digit), depth + 1)


        backtrack("", 0)
        return count[0]