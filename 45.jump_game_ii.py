class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        current_end = 0   # The range of our current jump
        farthest = 0    # Farthest potentially reachable distance
        jumps = 0   # Jumps so far

        for i in range(n-1):
            # Check if jumping from our current spot can get us farther
            farthest = max(farthest, i + nums[i])

            # Whenever i reaches current_end, we've exhausted the jump window
            # So we make the end of the next jump window farthest, since it's as far as we can go
            # Then we increment jumps
            if i == current_end:
                current_end = farthest
                jumps += 1

        return jumps