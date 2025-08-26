class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0 # Area of the rectangle with longest diagonal
        max_diag = 0    # The longest diagonal so far

        for l, w in dimensions:
            new_diag = l*l + w*w    # There's no need to get the actual length of the diagonal. Using the pythagoraus theorem, this is the diagonal squared, but that doesn't matter, because if a^2 > b^2, then logcally a > b
            area = l*w

            if new_diag > max_diag or (new_diag == max_diag and area > res):
                max_diag = new_diag
                res = area

        return res