from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort the envelopes by width ascemdomg and by height descending, so we compare only heights
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        largest = []  # largest[i] = the largest envelope in a chain i envelopes deep

        for _, h in envelopes:
            # Find the smallest height h can replace to make extending a chain of depth i easier
            i = bisect_left(largest, h)

            if i == len(largest):
                largest.append(h)
            else:
                largest[i] = h

        return len(largest)  # The length of the array is maximum number of envelopes we've managed to Russian doll