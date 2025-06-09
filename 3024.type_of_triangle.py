class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        s1, s2, s3 = nums

        if s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
            return "none"

        if s1 == s2:
            if s1 == s3:
                return "equilateral"
            return "isosceles"
        elif s3 == s1 or s3 == s2:
            return "isosceles"
        return "scalene"