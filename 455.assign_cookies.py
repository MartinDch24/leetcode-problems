#Resolved
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()    # Sort both the greed and sizes ascending
        s.sort()

        res = 0 # content children
        i = j = 0

        while i < len(g) and j < len(s):
            # Check if the current cookie satisfied the current child
            if s[j] >= g[i]:
                res += 1
                i += 1
                j += 1
            # If it doesn't, move onto the next cookie
            else:
                j += 1

        return res

        #Second solution:
            # g.sort()
            # s.sort()
            #
            # j = 0
            # n = len(g)
            #
            # for i in range(len(s)):
            #     if g[j] <= s[i]:
            #         j += 1
            #         if j >= n:
            #             break
            #
            # return j