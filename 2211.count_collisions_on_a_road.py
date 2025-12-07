class Solution:
    def countCollisions(self, directions: str) -> int:
        # Remove leading lefts and trailing rights, because they'll never collide
        i = 0
        while i < len(directions) and directions[i] == 'L':
            i += 1

        j = len(directions) - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1

        res = 0
        for k in range(i, j + 1):
            # Every other car that isn't stationary will have a collision
            if directions[k] != 'S':
                res += 1

        return res
