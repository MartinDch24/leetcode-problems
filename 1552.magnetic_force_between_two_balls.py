class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort() # Sort the positions

        left = 1    # Smallest possible distance
        right = position[-1] - position[0]  # Largest possible distance

        while left <= right:
            mid = (left+right)//2   # Candidate value
            i = 0   # Put the first ball in the first position
            curr_balls = 1

            for j in range(1, len(position)):
                # Put each ball at distance mid
                if position[j] - position[i] >= mid:
                    i = j
                    curr_balls += 1

            # Check if the balls we managed to fit are more or less than we need
            if curr_balls >= m:
                left = mid+1
            else:
                right = mid-1

        return right    # Last valid value