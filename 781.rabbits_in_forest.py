class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        num_set = Counter(answers)

        rabbits = 0
        for num, freq in num_set.items():
            group = num + 1
            rabbits += group * ((freq + num) // group)

        return rabbits