class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # Find the longest removable consecutive bars in each direction
        hBars.sort()
        vBars.sort()
        max_h, max_v = 1, 1
        curr = 1

        for i in range(1, len(hBars)):
            if hBars[i-1] + 1 == hBars[i]:
                curr += 1
            else:
                curr = 1
            max_h = max(max_h, curr)

        curr = 1

        for i in range(1, len(vBars)):
            if vBars[i-1] + 1 == vBars[i]:
                curr += 1
            else:
                curr = 1
            max_v = max(max_v, curr)

        # Side length = min removable bars + 1 (bars define cells)
        side = min(max_h, max_v) + 1

        return side * side