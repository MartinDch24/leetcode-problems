from collections import Counter


class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        freq = Counter(digits)
        res = set()

        for i in range(1, 10):
            if freq[i] == 0:
                continue
            freq[i] -= 1

            for j in range(0, 10):
                if freq[j] == 0:
                    continue
                freq[j] -= 1

                for k in [0, 2, 4, 6, 8]:
                    if freq[k] > 0:
                        res.add(i * 100 + j * 10 + k)

                freq[j] += 1
            freq[i] += 1

        return sorted(res)