class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefixes = [0]
        for diff in differences:
            prefixes.append(prefixes[-1] + diff)

        return max(0, upper - max(prefixes) - lower + min(prefixes) + 1)