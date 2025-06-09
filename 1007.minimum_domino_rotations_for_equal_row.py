class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        n = len(tops)
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(n):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        res = min(check(tops[0]), check(bottoms[0]) if tops[0] != bottoms[0] else float('inf'))
        return res if res != float('inf') else -1